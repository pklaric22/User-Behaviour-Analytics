# User Behaviour Analytics (UBA)
User Behavior Analytics (UBA) u kibernetičkoj sigurnosti označava skup metoda i alata koji koriste analitiku podataka, umjetnu inteligenciju i strojno učenje za praćenje ponašanja korisnika u mreži, modeliranje njihovih uobičajenih obrazaca te detekciju odstupanja koja mogu ukazivati na sigurnosne prijetnje. U praksi to znači da UBA sustav kontinuirano prikuplja podatke o prijavama, pristupu resursima (npr. pristup zaposlenika na portalima poduzeća), mrežnim tokovima i drugim aktivnostima, kako bi izgradio baznu liniju “normalnog” ponašanja za svakog korisnika.

## Korisnička aktivnost
Korisnička aktivnost predstavlja osnovnu jedinicu podataka koju UBA sustavi prikupljaju i analiziraju, pri čemu svaki događaj predstavlja konkretnu radnju korisnika u digitalnom okruženju. To su svi digitalni tragovi koje korisnik ostavlja tijekom interakcije s mrežnim resursima, aplikacijama i podacima unutar sustava, poput prijava, pristupa datotekama, promjene postavki ili mrežnih zahtjeva prema određenim servisima.

Umjesto pukog bilježenja tehničkih događaja, UBA sustavi nastoje svaki događaj staviti u kontekst – tko je radnju izvršio, kada, s kojeg uređaja ili lokacije, pod kojim ovlastima i u kojem poslovnom procesu. Na taj način aktivnosti prestaju biti izolirani log zapisi i postaju dio ponašanja konkretne osobe ili automatiziranog procesa, što je ključno za prepoznavanje odstupanja i potencijalno zlonamjernog ponašanja.

Glavni izvori podataka o korisničkoj aktivnosti u sigurnosnom kontekstu uključuju:
- autentifikacijske zapise (prijave, odjave, neuspjele pokušaje, MFA),
- trajanje sesije,
- operacije nad datotekama (čitanje, pisanje, brisanje, preuzimanje),
- mrežnu aktivnost (protokoli, odredišne IP adrese, količina podataka) te
- korištenje aplikacija i administrativnih alata (stranice koje se pregledavaju, mjesta koja se najčešće klikaju).

## Uzorci ponašanja (eng. _behaviour patterns_) korisnika
Dok je korisnička aktivnost sirovi podatak, uzorci ponašanja (eng. _behavior patterns_) predstavljaju modelirane obrasce koji nastaju kada se te aktivnosti analiziraju kroz vrijeme. UBA sustav na temelju povijesnih logova gradi "normalno" ponašanje za svakog korisnika ili ulogu (npr. administrator, računovođa, developer), definirajući što je uobičajeno u pogledu vremena, lokacije, resursa i intenziteta aktivnosti. Ovi uzorci obično se promatraju kroz nekoliko ključnih dimenzija:
- **Vremenski obrasci (kada):** tipično radno vrijeme, sezonalnost aktivnosti, uobičajeni ritam prijava i pristupa resursima.
- **Operativni obrasci (što i kako)**: koje aplikacije i servise korisnik koristi, koje tipove datoteka obrađuje, kakve su mu uobičajene operacije nad podacima.
- **Geografski/infrastrukturni obrasci (odakle):** uobičajene IP adrese, uređaji, VPN-ovi i mrežni segmenti s kojih se korisnik spaja, uključujući prepoznavanje “nemogućeg putovanja”.

Kombinacijom ovih faktora UBA sustavi dodjeljuju bodove rizika određenim odstupanjima od uobičajenih uzoraka, pri čemu veća devijacija od bazne linije znači i viši rizik. Na taj način se iz mase svakodnevnih aktivnosti izdvajaju potencijalno opasni scenariji, poput kompromitiranih vjerodajnica, zlonamjernih insajdera ili naprednih trajnih prijetnji, čime se sigurnosnim timovima omogućuje fokus na najkritičnije incidente.

<br>

<p align="center">
  <img width="1408" height="768" alt="Gemini_Generated_Image_quxxr5quxxr5quxx" src="https://github.com/user-attachments/assets/c13184f7-0373-4861-9019-fa89be7dd794" />
  <br>
  <em>Slika 1: Model UBA sustava (Izvor: generirano s UI alatom gemini.google.com)</em>
</p>

<br>

## Anomalije i strojno učenje

Anomalije u kontekstu User Behaviour Analytics sustava predstavljaju odstupanja od uobičajenih obrazaca ponašanja korisnika. Takva odstupanja ne moraju nužno uvijek označavati zlonamjernu aktivnost, ali mogu ukazivati na povećani sigurnosni rizik, osobito ako se ponavljaju ili kombiniraju s drugim neuobičajenim događajima. Primjeri anomalija uključuju prijave iz neuobičajenih geografskih lokacija, nagli porast broja zahtjeva u kratkom vremenskom razdoblju ili pristup resursima koji nisu dio uobičajenog radnog procesa korisnika.

U suvremenim UBA sustavima često se primjenjuju tehnike strojnog učenja kako bi se automatizirala detekcija anomalija. Modeli strojnog učenja mogu se trenirati na povijesnim podacima kako bi naučili normalne obrasce ponašanja te prepoznali odstupanja bez potrebe za ručno definiranim pravilima. Najčešće se koriste nenadzirane metode učenja, budući da unaprijed označeni podaci o napadima često nisu dostupni.

U okviru ovog projekta strojno učenje nije implementirano, već je primijenjen jednostavniji pristup temeljen na pragovima i ponašajnim pravilima. Takav pristup omogućuje jasnu interpretaciju rezultata i lakše razumijevanje procesa detekcije anomalija, što je posebno prikladno u edukativnom kontekstu.


## Virtualno okruženje

Za potrebe implementacije i testiranja User Behaviour Analytics sustava korišteno je virtualno okruženje temeljeno na dvije odvojene virtualne mašine. Takva arhitektura omogućuje jasnu razdvojenost između poslužiteljskog dijela sustava i klijentskih aktivnosti, čime se vjernije simulira stvarno mrežno okruženje.

Prva virtualna mašina korištena je kao serversko okruženje te je na njoj pokrenuta ciljana aplikacija zajedno s pripadajućim sustavima za prikupljanje metrika i nadzor sigurnosnih događaja. U tom okruženju generiraju se zapisi i metrike koji opisuju ponašanje korisnika, kao i sigurnosni događaji relevantni za analizu.

Druga virtualna mašina korištena je za simulaciju klijentskih aktivnosti. Na njoj su izvođene kontrolirane simulacije korisničkog ponašanja, uključujući normalne aktivnosti i anomalne scenarije. Na taj način omogućeno je generiranje realističnog prometa prema serverskom sustavu, bez izravnog utjecaja na stabilnost i integritet poslužiteljskog okruženja.

