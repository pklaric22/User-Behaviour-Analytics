# User Behaviour Analytics
## Overview of the project
User Behavior Analytics (UBA) fokusira se na prikupljanje i analizu podataka o aktivnostima korisnika na mreži, uključujući prijave, pristup datotekama i mrežne tokove. Za razliku od tradicionalnih sigurnosnih sustava koji prepoznaju isključivo poznate prijetnje, UBA sustavi koriste povijesne podatke i metode strojnog učenja za detekciju odstupanja od "normalnog" ponašanja korisnika, čime se mogu pravovremeno uočiti kompromitirani računi ili unutarnje prijetnje (eng. insider threats). Sukladno tome, cilj ovog projekta je teorijski objasniti i praktično demonstrirati UBA pristup unutar kontroliranog virtualnog mrežnog okruženja, a u praktičnom dijelu projekta implementirat će se sustav za praćenje ponašanja korisnika koristeći Oracle VirtualBox, GNS3, SELKS stack i VS Code.

## Project team
Name and surname | E-mail address (FOI) | JMBAG | Github username
---------------  | -------------------- | ----- | ---------------
Patrik | pklaric22@student.foi.hr |  | pklaric22
Jure | jjelcic22@student.foi.hr |  | jjelcic22
Maks | mkos22@student.foi.hr |  | mkos22
Marta Kovač | mkovac21@student.foi.hr | 0016154537 | mkovac21

## Ciljevi projekta
Glavni ciljevi projekta su:
- simulirati realistično okruženje s korisničkim aktivnostima
- prikupljati i analizirati podatke o ponašanju korisnika
- identificirati anomalije i potencijalno zlonamjerne aktivnosti
- vizualizirati sigurnosne metrike i događaje
- evaluirati učinkovitost ponašajno orijentiranog pristupa detekciji napada

---

## Korištene tehnologije i alati
U sklopu projekta korišteni su sljedeći alati:
- **Prometheus** – prikupljanje i nadzor metrika
- **Grafana** – vizualizacija podataka i izrada nadzornih ploča
- **Locust** – simulacija korisničkog ponašanja i napadačkog prometa
- **Flask** – backend aplikacija koja simulira ciljani sustav

---

## Opseg projekta
Projekt je usmjeren na **detekciju anomalija temeljenu na ponašanju korisnika**.

Anomalije se identificiraju korištenjem pragova i obrazaca ponašanja dobivenih analizom prikupljenih metrika.  
Primjena strojnog učenja razmatra se kao mogući budući nastavak projekta, ali nije implementirana u trenutnoj verziji.

---

## Struktura repozitorija
Repozitorij je organiziran na sljedeći način:
- `docs/` – teorijska podloga, plan implementacije i završno izvješće
- `implementation/` – izvorni kod, konfiguracijske datoteke i upute za postavljanje
- `results/` – rezultati, zapisi, snimke zaslona i analiza
- `presentation/` – prezentacijski materijali projekta


