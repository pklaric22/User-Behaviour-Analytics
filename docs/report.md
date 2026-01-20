## 1. Opis implementacije
### 1.1 Virtualno okruženje

Za implementaciju projekta korišteno je virtualno okruženje temeljeno na dvije odvojene virtualne mašine, čime se omogućila jasna separacija između poslužiteljskog sustava i klijentskih aktivnosti. Takva arhitektura vjernije simulira stvarno korporativno mrežno okruženje te omogućuje kontrolirano generiranje i analizu prometa.

Prva virtualna mašina korištena je kao serversko okruženje, na kojem je pokrenuta aplikacija temeljena na Flask frameworku. Uz aplikaciju su implementirani sustavi za prikupljanje metrika i nadzor ponašanja korisnika.

Druga virtualna mašina korištena je za simulaciju klijentskih aktivnosti, uključujući normalno ponašanje korisnika i različite napadačke scenarije. Ovakav pristup omogućio je realističan promet prema serveru bez ugrožavanja stabilnosti poslužiteljskog sustava.

### 1.2 Serverska aplikacija i UBA logika

Serverski dio projekta implementiran je korištenjem Flask web frameworka. Aplikacija izlaže više REST API endpointa (`/api/health`, `/api/data`, `/api/profile`, `/api/login`, `/api/admin`) koji simuliraju tipične funkcionalnosti aplikacijskog sustava i generiraju sigurnosno relevantne događaje.

Unutar serverske aplikacije implementirana je **rule-based User Behaviour Analytics (UBA) logika** koja u stvarnom vremenu analizira ponašanje korisnika na temelju njihove IP adrese. Sustav kontinuirano prati učestalost HTTP zahtjeva u kratkom vremenskom razdoblju, broj neuspješnih pokušaja prijave te broj različitih endpointa kojima pojedini korisnik pristupa.

Na temelju prikupljenih podataka korisnici se klasificiraju u jednu od sljedeće tri uloge:

- `normal`
- `suspicious`
- `attacker`

Svaka promjena uloge bilježi se i izlaže kroz **Prometheus metrike**, što omogućuje daljnju analizu ponašanja korisnika i vizualizaciju sigurnosnih događaja putem Grafana nadzornih ploča.

Uz UBA logiku implementiran je i **mehanizam lockout zaštite**, koji privremeno blokira korisnika nakon prevelikog broja neuspješnih pokušaja prijave. Time se simulira obrambeni mehanizam protiv brute-force napada te dodatno povećava sigurnost aplikacijskog sustava.

### 1.3 Klijentska simulacija ponašanja

Za simulaciju korisničkog ponašanja korišten je alat **Locust**, koji omogućuje generiranje velikog broja istovremenih HTTP zahtjeva prema serverskoj aplikaciji. Locust omogućuje definiranje različitih tipova ponašanja unutar jedne simulacije, čime se postiže realističan model korisničkih aktivnosti.

U okviru simulacije implementirana su sljedeća ponašanja:

- normalne korisničke aktivnosti, uključujući pregled profila, dohvat podataka i provjeru stanja sustava
- legitimna prijava korisnika
- brute-force napad na endpoint za prijavu
- skeniranje dostupnih API endpointa (reconnaissance)

Omjeri pojedinih aktivnosti pažljivo su odabrani kako bi se postigla realistična kombinacija legitimnog i zlonamjernog ponašanja korisnika, što omogućuje učinkovito testiranje UBA mehanizama implementiranih na serverskoj strani.

---

## 2. Vizualizacija i praćenje metrika

Za prikupljanje i vizualizaciju podataka korišteni su alati **Prometheus** i **Grafana**. Serverska aplikacija izlaže niz metrika koje Prometheus automatski prikuplja, dok se Grafana koristi za njihov grafički prikaz i analizu.

Putem Grafana nadzornih ploča moguće je pratiti:
- ukupan broj zahtjeva po minuti
- raspodjelu HTTP status kodova (200, 401, 403, 429)
- broj zahtjeva po pojedinim API endpointima
- broj grešaka u sekundi
- prosječno vrijeme odgovora aplikacije

Priloženi Grafana screenshotovi jasno prikazuju porast broja neuspješnih prijava i HTTP 429 odgovora tijekom izvođenja brute-force napada, kao i povećanu učestalost pristupa različitim endpointima tijekom faze skeniranja. Ovi podaci potvrđuju ispravnost prikupljanja metrika i učinkovitost sustava za nadzor sigurnosnih događaja.

## 3. Detekcija anomalija i reakcija sustava

Tijekom izvođenja simulacija sustav je uspješno detektirao anomalna ponašanja korisnika. Terminalski isječci i prikupljene metrike jasno prikazuju aktivaciju pravila za veliki broj neuspješnih pokušaja prijave, detekciju skeniranja dostupnih API endpointa te promjene uloge korisnika iz `normal` u `suspicious` i `attacker`.

Osim detekcije anomalija, sustav je automatski reagirao aktivacijom **lockout mehanizma**, kojim se privremeno blokiraju korisnici s prevelikim brojem neuspješnih pokušaja prijave. Ovakva reakcija simulira stvarne obrambene mehanizme koji se koriste za zaštitu aplikacijskih sustava od brute-force napada.

Na temelju dobivenih rezultata može se zaključiti da implementirani UBA mehanizam uspješno identificira neuobičajene obrasce ponašanja i reagira u stvarnom vremenu, čime se povećava ukupna razina sigurnosti sustava.

---

## 4. Odstupanja od početnog plana

Početni plan projekta predviđao je korištenje alata poput SELKS stacka i GNS3-a, kao i implementaciju modela strojnog učenja za detekciju anomalija.
Tijekom realizacije projekta došlo je do određenih odstupanja od planiranog pristupa, prvenstveno zbog složenosti postavljanja mrežnih konfiguracija i rada s Docker kontejnerima u zadanom vremenskom okviru projekta. Zbog navedenih tehničkih ograničenja arhitektura sustava je pojednostavljena te je implementiran rule-based UBA pristup uz korištenje alata Prometheus i Grafana, koji su omogućili stabilno izvođenje sustava i jasnu analizu ponašanja korisnika.


---

## 5. Zaključak

U okviru ovog projekta uspješno je implementiran sustav za User Behaviour Analytics koji omogućuje detekciju neuobičajenog i potencijalno zlonamjernog ponašanja korisnika unutar kontroliranog virtualnog okruženja.

Dobiveni rezultati potvrđuju da UBA predstavlja vrijedan dodatak tradicionalnim sigurnosnim mehanizmima, osobito u scenarijima koji uključuju kompromitirane korisničke račune.
