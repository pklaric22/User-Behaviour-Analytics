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

<p align="center">
  <img width="1408" height="768" alt="Gemini_Generated_Image_quxxr5quxxr5quxx" src="https://github.com/user-attachments/assets/c13184f7-0373-4861-9019-fa89be7dd794" />
  <br>
  <em>Slika 1: Model UBA sustava (Izvor: generirano s UI alatom gemini.google.com)</em>
</p>

<br>

## Anomalije i strojno učenje

## Virtualno okruženje

