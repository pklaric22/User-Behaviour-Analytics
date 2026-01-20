# Upute za pokretanje sustava

Ovaj dokument opisuje korake potrebne za pokretanje sustava za User Behaviour Analytics (UBA) u kontroliranom virtualnom okruženju.

---

## 1. Instalacija Oracle VirtualBoxa

Na host računalu potrebno je instalirati **Oracle VirtualBox**, koji se koristi za pokretanje virtualnih mašina. Instalacijski paket može se preuzeti sa službene web stranice proizvođača, nakon čega je potrebno slijediti standardni postupak instalacije.

---

## 2. Postavljanje virtualnih mašina

Potrebno je kreirati **dvije virtualne mašine** s operacijskim sustavom **Ubuntu Linux**:

- **Server VM** – pokreće Flask aplikaciju, Prometheus i Grafanu  
- **Client VM** – koristi se za simulaciju korisničkih aktivnosti i napada  

Preporučene minimalne postavke za svaku virtualnu mašinu:
- 2 CPU jezgre  
- 2–4 GB RAM-a  
- 20 GB prostora na disku  

---

## 3. Mrežne postavke

Za obje virtualne mašine potrebno je postaviti mrežni adapter na način rada **Bridged Adapter**. Ova postavka omogućuje da se virtualne mašine nalaze u istoj mreži te mogu međusobno komunicirati putem IP adresa.

Provjera IP adrese na virtualnoj mašini (naredba je zakomentirana):

`# ip a`

---

## 4. Pokretanje Prometheus servisa

Na serverskoj virtualnoj mašini potrebno je pokrenuti Prometheus servis, koji služi za prikupljanje metrika iz Flask aplikacije.

`# sudo systemctl start prometheus`

Provjera statusa servisa:

`# sudo systemctl status prometheus`

---

## 5. Pokretanje Grafana servisa

Nakon pokretanja Prometheusa potrebno je pokrenuti Grafana server.

`# sudo systemctl start grafana-server`

Grafana web sučelje dostupno je putem preglednika na adresi:

`http://<IP_adresa_servera>:3000`

Zadani podaci za prijavu su:
- korisničko ime: `admin`  
- lozinka: `admin`  

---

## 6. Povezivanje Grafane s Prometheusom

Za povezivanje Grafane s Prometheusom potrebno je izvršiti sljedeće korake u Grafana web sučelju:

1. Otvoriti **Configuration → Data sources**
2. Odabrati **Add data source**
3. Izabrati **Prometheus**
4. U polje **URL** unijeti:  
   `http://localhost:9090`
5. Kliknuti **Save & Test**

Uspješna poruka potvrđuje ispravnu povezanost Grafane s Prometheusom.

---

## 7. Pokretanje serverske aplikacije

Na serverskoj virtualnoj mašini potrebno je pokrenuti Flask aplikaciju koja implementira UBA logiku.

`# python3 server.py`

Serverska aplikacija sluša na portu `8000` te izlaže metrike koje Prometheus periodički prikuplja.

---

## 8. Pokretanje klijentske simulacije

Na klijentskoj virtualnoj mašini pokreće se simulacija korisničkog ponašanja pomoću alata **Locust**.

Locust se pokreće iz direktorija koji sadrži klijentsku skriptu, pri čemu se ciljana IP adresa serverske aplikacije definira prilikom pokretanja:

`# locust -f klijent.py -H http://<IP_adresa_servera>:8000`

Nakon pokretanja Locusta dostupno je web sučelje na adresi:

`http://<IP_adresa_klijenta>:8089`

Putem web sučelja definiraju se parametri simulacije (broj korisnika i brzina generiranja zahtjeva), nakon čega se simulacija pokreće.

---

## 9. Praćenje rada sustava

Tijekom izvođenja simulacije moguće je u stvarnom vremenu pratiti ponašanje sustava:

- Grafana prikazuje metrike i sigurnosne događaje
- Prometheus prikuplja podatke o zahtjevima i klasifikaciji korisnika
- Serverski terminal ispisuje UBA detekcije i promjene uloga korisnika

