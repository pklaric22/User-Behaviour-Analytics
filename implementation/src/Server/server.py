from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime, timedelta
import time
import os
from collections import defaultdict, deque
import random

from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter

DB_PATH = "database/events.db"

def now_iso():
    return datetime.utcnow().isoformat()

def get_ip():
    return request.headers.get("X-Forwarded-For", request.remote_addr) or "unknown"

def db_execute(query, params=(), fetch=False):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(query, params)
    rows = cur.fetchall() if fetch else None
    con.commit()
    con.close()
    return rows

def ensure_db_folder():
    folder = os.path.dirname(DB_PATH)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

def useDatabase():
    ensure_db_folder()
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS login_attempts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL,
            ip TEXT NOT NULL,
            username TEXT NOT NULL,
            success INTEGER NOT NULL
        )
    """)

    cur.execute("INSERT OR IGNORE INTO users(username, password) VALUES(?,?)", ("demo", "demo123"))

    con.commit()
    con.close()

req_times = defaultdict(lambda: deque(maxlen=2000))
fail_times = defaultdict(lambda: deque(maxlen=2000))
endpoint_hits = defaultdict(lambda: deque(maxlen=2000))
current_role = defaultdict(lambda: "normal")

REQ_WINDOW_SEC = 10
REQ_SUSPICIOUS = 15
REQ_ATTACKER = 25

FAIL_WINDOW_SEC = 60
FAIL_SUSPICIOUS = 5
FAIL_ATTACKER = 12

ENDPOINT_WINDOW_SEC = 30
ENDPOINT_UNIQUE_SUSPICIOUS = 4
ENDPOINT_UNIQUE_ATTACKER = 7

LOCKOUT_THRESHOLD = 10

def _purge_old_ts(dq: deque, older_than_ts: float):
    while dq and dq[0] < older_than_ts:
        dq.popleft()

def _purge_old_endpoint_hits(dq: deque, older_than_ts: float):
    while dq and dq[0][0] < older_than_ts:
        dq.popleft()

def classify_ip(ip: str):
    """
    Vraća: (role, reason)
    role: normal / suspicious / attacker
    reason: baseline / many_failed_logins / request_flood / endpoint_scan / ...
    """
    now_ts = time.time()

    _purge_old_ts(req_times[ip], now_ts - REQ_WINDOW_SEC)
    _purge_old_ts(fail_times[ip], now_ts - FAIL_WINDOW_SEC)
    _purge_old_endpoint_hits(endpoint_hits[ip], now_ts - ENDPOINT_WINDOW_SEC)

    r10 = len(req_times[ip])
    f60 = len(fail_times[ip])
    unique_eps = len({ep for _, ep in endpoint_hits[ip]})

    if f60 >= FAIL_ATTACKER:
        return "attacker", "many_failed_logins"
    if r10 >= REQ_ATTACKER:
        return "attacker", "request_flood"
    if unique_eps >= ENDPOINT_UNIQUE_ATTACKER:
        return "attacker", "endpoint_scan"

    if f60 >= FAIL_SUSPICIOUS:
        return "suspicious", "failed_logins_spike"
    if r10 >= REQ_SUSPICIOUS:
        return "suspicious", "high_request_rate"
    if unique_eps >= ENDPOINT_UNIQUE_SUSPICIOUS:
        return "suspicious", "many_endpoints"

    return "normal", "baseline"

app = Flask(__name__)

metrics = PrometheusMetrics(app)

UBA_ROLE_CHANGES = Counter(
    "uba_role_changes_total",
    "Number of role changes detected by UBA logic",
    ["ip", "role_old", "role_new", "reason"]
)

UBA_AUTH_ATTEMPTS = Counter(
    "uba_auth_attempts_total",
    "Number of authentication attempts",
    ["ip", "username", "success"]
)

UBA_AUTH_LOCKOUTS = Counter(
    "uba_auth_lockouts_total",
    "Number of lockout events",
    ["ip", "username"]
)

UBA_CLASSIFIED_REQUESTS = Counter(
    "uba_classified_requests_total",
    "Number of requests classified by UBA role",
    ["ip", "role", "endpoint", "method", "status"]
)

UBA_RULE_HITS = Counter(
    "uba_rule_hits_total",
    "Number of times a UBA rule triggered (reason)",
    ["ip", "reason"]
)

def maybe_emit_role_change(ip: str, new_role: str, reason: str):
    old_role = current_role[ip]
    if new_role != old_role:
        current_role[ip] = new_role

        print(
            f"[UBA] ROLE CHANGE | ip={ip} {old_role}->{new_role} | reason={reason} | "
            f"req_10s={len(req_times[ip])} fails_60s={len(fail_times[ip])} "
            f"unique_eps_30s={len({ep for _, ep in endpoint_hits[ip]})} | ts={now_iso()}"
        )

        try:
            UBA_ROLE_CHANGES.labels(
                ip=ip, role_old=old_role, role_new=new_role, reason=reason
            ).inc()
        except Exception:
            pass

@app.route("/")
def hello():
    return "<h1>SIS UBA Project!</h1>"

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200

@app.route("/api/data", methods=["GET"])
def data():
    if random.random() < 0.1:
        time.sleep(0.2)
    return jsonify({"items": [1, 2, 3]}), 200

@app.route("/api/profile", methods=["GET"])
def profile():
    return jsonify({"user": "demo", "role": "user", "msg": "profile loaded"}), 200

@app.route("/api/admin", methods=["GET"])
def admin():
    return jsonify({"ok": False, "error": "forbidden"}), 403

@app.before_request
def start_timer():
    request._start_time = time.time()
    ip = get_ip()
    req_times[ip].append(time.time())
    endpoint_hits[ip].append((time.time(), request.path))

@app.after_request
def log_request(response):
    ip = get_ip()
    role, reason = classify_ip(ip)
    maybe_emit_role_change(ip, role, reason)

    if reason != "baseline":
        try:
            UBA_RULE_HITS.labels(ip=ip, reason=reason).inc()
        except Exception:
            pass
        print(
            f"[UBA] RULE HIT | ip={ip} rule={reason} endpoint={request.path} status={response.status_code}"
        )

    try:
        UBA_CLASSIFIED_REQUESTS.labels(
            ip=ip, role=role, endpoint=request.path, method=request.method, status=str(response.status_code)
        ).inc()
    except Exception:
        pass

    return response

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    ip = get_ip()
    ts = now_iso()

    one_min_ago = (datetime.utcnow() - timedelta(seconds=FAIL_WINDOW_SEC)).isoformat()
    fails_db = db_execute(
        "SELECT COUNT(*) FROM login_attempts WHERE ip=? AND success=0 AND time>=?",
        (ip, one_min_ago),
        fetch=True
    )[0][0]

    if fails_db >= LOCKOUT_THRESHOLD:
        fail_times[ip].append(time.time())

        role, reason = classify_ip(ip)
        maybe_emit_role_change(ip, role, reason)

        try:
            UBA_AUTH_LOCKOUTS.labels(ip=ip, username=username).inc()
        except Exception:
            pass

        print(f"[AUTH] LOCKOUT | ip={ip} username={username} fails_last_60s={fails_db} ts={ts}")
        return jsonify({"ok": False, "error": "too_many_attempts"}), 429

    user = db_execute("SELECT password FROM users WHERE username=?", (username,), fetch=True)
    ok = (len(user) == 1 and user[0][0] == password)

    db_execute(
        "INSERT INTO login_attempts(time, ip, username, success) VALUES(?,?,?,?)",
        (ts, ip, username, 1 if ok else 0),
        fetch=False
    )

    note = ""
    if not ok:
        fail_times[ip].append(time.time())
        note = "invalid_credentials"

    role, reason = classify_ip(ip)
    maybe_emit_role_change(ip, role, reason)

    try:
        UBA_AUTH_ATTEMPTS.labels(ip=ip, username=username, success=str(1 if ok else 0)).inc()
    except Exception:
        pass

    if ok:
        return jsonify({"ok": True, "user": username}), 200
    return jsonify({"ok": False, "error": "invalid_credentials", "note": note}), 401

if __name__ == "__main__":
    useDatabase()
    app.run(host="0.0.0.0", port=8000, debug=False)
