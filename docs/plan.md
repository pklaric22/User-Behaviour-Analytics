# Praktični plan rada
Praktični dio projekta provodi se u kontroliranom virtualnom mrežnom okruženju kako bi se simuliralo tipično korporativno okruženje s više sustava i korisnika. U tu svrhu koriste se alati Oracle VirtualBox, GNS3, SELKS stack i VS Code, koji zajedno omogućuju virtualizaciju infrastrukture, nadzor mrežnog prometa, vizualizaciju podataka i razvoj modela strojnog učenja za detekciju anomalija. Konkretno, praktični dio projekta (Slika 1) može se sažeti u sljedećih pet koraka:
1. Uspostavljanje virtualne mreže
2. Dodjeljivanje uloga korisnicima u mreži
3. Praćenje mrežnog prometa
4. Izrada vizualizacije
5. Razvoj modela strojnog učenja za detekciju anomalija

<p align="center">
  <img width="1408" alt="Gemini_Generated_Image_b709p6b709p6b709" src="https://github.com/user-attachments/assets/b713383d-0fd4-4c3c-9c7e-320e23a1a7a7" />
  <br>
  <em>Slika 1: Praktični plan rada (Izvor: generirano s UI alatom gemini.google.com)</em>
</p>

<br>


**Uspostavljanje virtualne mreže:** Kao prvi korak, postavlja se virtualna infrastruktura koja će služiti kao testno okruženje za UBA. Oracle VirtualBox, kao hipervizor tipa 2, koristi se za kreiranje i upravljanje virtualnim strojevima koji emuliraju poslužitelje i klijentska računala, dok se pomoću GNS3-a simulira mrežna topologija (usmjerivači, prekidači, segmenti mreže) i definira način na koji su sustavi međusobno povezani.

**Dodjeljivanje uloga korisnicima u mreži:** Nakon uspostave mreže definiraju se različite korisničke uloge (npr. administrator, obični korisnik, analitičar) i odgovarajuće razine pristupa resursima. Svaka uloga dobiva specifične vjerodajnice i tipične zadatke, čime se simulira stvarno poslovno okruženje i omogućuje kasnija izgradnja uzoraka ponašanja pojedinih profila korisnika unutar UBA sustava.

**Praćenje mrežnog prometa:** U trećoj fazi na virtualnu mrežu uvodi se SELKS stack kao centralna platforma za nadzor i analizu mrežnog prometa. Suricata se koristi za dubinsku inspekciju paketa i detekciju sumnjivih mrežnih obrazaca, Logstash za obradu i prosljeđivanje logova, Elasticsearch za pohranu i pretraživanje događaja, dok SuriCata i ostale komponente omogućuju korelaciju aktivnosti korisnika s mrežnim tokovima

**Izrada vizualizacije:** Kako bi se prikupljeni podaci učinili razumljivima i preglednima, koristi se Kibana kao dio SELKS stacka za izradu interaktivnih nadzornih ploča. Na ovim se vizualizacijama prikazuju ključni pokazatelji poput broja prijava, distribucije mrežnog prometa, tipova detektiranih događaja i rizika po korisniku, što olakšava prepoznavanje anomalnog ponašanja i izvještavanje o rezultatima.

**Razvoj modela strojnog učenja za detekciju anomalija:** U završnom koraku, odabrani skup podataka o korisničkim aktivnostima i mrežnom prometu koristi se za izgradnju modela strojnog učenja za detekciju anomalija. U okruženju VS Code razvijaju se skripte, koristeći Python programski jezik, koje primjenjuju metode nenadziranog učenja ili modela za otkrivanje odstupanja, a rezultati se zatim uspoređuju s detekcijama dobivenima iz SELKS-a kako bi se evaluirala učinkovitost kombiniranog pristupa UBA i ML tehnika.


