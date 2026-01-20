from locust import HttpUser, task, between
import random


class MixedUser(HttpUser):
   wait_time = between(1.0, 25.0)


   @task(6)
   def health(self):
       with self.client.get("/api/health", name="/api/health", catch_response=True) as r:
           if r.status_code != 200:
               r.failure(f"Unexpected status: {r.status_code}")


   @task(4)
   def browse_data(self):
       with self.client.get("/api/data", name="/api/data", catch_response=True) as r:
           if r.status_code != 200:
               r.failure(f"Unexpected status: {r.status_code}")


   @task(3)
   def profile(self):
       with self.client.get("/api/profile", name="/api/profile", catch_response=True) as r:
           if r.status_code != 200:
               r.failure(f"Unexpected status: {r.status_code}")


   @task(2)
   def login_ok(self):
       with self.client.post(
           "/api/login",
           json={"username": "demo", "password": "demo123"},
           name="/api/login_ok",
           catch_response=True,
       ) as r:
           if r.status_code != 200:
               r.failure(f"Expected 200, got {r.status_code}")


   @task(1)
   def brute_force_login(self):
       with self.client.post(
           "/api/login",
           json={"username": "demo", "password": f"wrong{random.randint(1, 999999)}"},
           name="/api/login_fail",
           catch_response=True,
       ) as r:
           if r.status_code not in (401, 429):
               r.failure(f"Expected 401/429, got {r.status_code}")


   @task(1)
   def endpoint_scan(self):
       paths = ["/api/health", "/api/data", "/api/profile", "/api/admin"]
       target = random.choice(paths)
       with self.client.get(target, name="/api/scan", catch_response=True) as r:
           if target == "/api/admin":
               if r.status_code != 403:
                   r.failure(f"Expected 403 for /api/admin, got {r.status_code}")
           else:
               if r.status_code != 200:
                   r.failure(f"Expected 200, got {r.status_code}")






