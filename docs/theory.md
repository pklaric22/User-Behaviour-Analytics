# User Behaviour Analytics (UBA)

User Behaviour Analytics (UBA) u području kibernetičke sigurnosti označava skup metoda i alata koji koriste analitiku podataka, statističke tehnike te metode umjetne inteligencije i strojnog učenja za praćenje i analizu ponašanja korisnika unutar informacijskog sustava. Cilj UBA pristupa je modelirati uobičajene obrasce ponašanja korisnika i na temelju njih prepoznati odstupanja koja mogu ukazivati na sigurnosne prijetnje, poput kompromitiranih korisničkih računa ili zloupotrebe ovlasti [1].

U praksi, UBA sustav kontinuirano prikuplja podatke o prijavama korisnika, pristupu resursima, mrežnim tokovima i drugim interakcijama unutar sustava. Na temelju tih podataka izgrađuje se bazna linija normalnog ponašanja za svakog korisnika ili korisničku ulogu, što omogućuje prepoznavanje neuobičajenih aktivnosti u stvarnom vremenu [2].

---

## Korisnička aktivnost

Korisnička aktivnost predstavlja temeljnu jedinicu podataka koju UBA sustavi prikupljaju i analiziraju. Svaka aktivnost odgovara konkretnoj radnji korisnika u digitalnom okruženju te obuhvaća sve digitalne tragove nastale tijekom interakcije s mrežnim resursima, aplikacijama i podacima unutar sustava. Takve aktivnosti uključuju autentifikacijske događaje, pristup datotekama, promjene konfiguracija, kao i mrežne zahtjeve prema različitim servisima [3].

Za razliku od klasičnog pristupa koji se svodi na puko bilježenje tehničkih logova, UBA sustavi nastoje svaku aktivnost staviti u širi kontekst. To uključuje identitet korisnika, vrijeme izvršavanja radnje, korišteni uređaj ili lokaciju, dodijeljene ovlasti te poslovni kontekst u kojem se aktivnost odvija. Time pojedinačni događaji prestaju biti izolirani zapisi i postaju dio cjelovitog obrasca ponašanja određenog korisnika ili procesa, što je ključno za učinkovitu detekciju anomalija i potencijalno zlonamjernog ponašanja [4].

---

## Uzorci ponašanja korisnika

Dok korisnička aktivnost predstavlja sirove podatke, uzorci ponašanja korisnika nastaju analizom tih aktivnosti kroz dulje vremensko razdoblje. UBA sustavi na temelju povijesnih zapisa oblikuju model normalnog ponašanja za pojedinog korisnika ili skupinu korisnika sličnih uloga, poput administratora, računovođa ili razvojnih inženjera. Takvi modeli definiraju što se smatra uobičajenim u pogledu vremena, lokacije, resursa i intenziteta aktivnosti [1].

Uzorci ponašanja obično uključuju vremenske aspekte, poput tipičnog radnog vremena i učestalosti prijava, operativne aspekte koji opisuju koje aplikacije i resurse korisnik koristi te infrastrukturne ili geografske aspekte, kao što su uobičajene IP adrese, uređaji i mrežni segmenti s kojih se korisnik povezuje. Kombinacijom tih dimenzija UBA sustavi mogu prepoznati situacije koje značajno odstupaju od očekivanog ponašanja, poput prijava s neuobičajenih lokacija ili naglog povećanja aktivnosti [5].

Na temelju odstupanja od bazne linije ponašanja, UBA sustavi često dodjeljuju bodove rizika pojedinim događajima ili korisnicima. Veća devijacija od uobičajenih obrazaca rezultira višom razinom rizika, čime se sigurnosnim timovima omogućuje da se fokusiraju na potencijalno najopasnije scenarije, uključujući kompromitirane vjerodajnice, insajderske prijetnje i napredne trajne napade.
<br>

<p align="center">
  <img width="1408" height="768" alt="Gemini_Generated_Image_quxxr5quxxr5quxx" src="https://github.com/user-attachments/assets/c13184f7-0373-4861-9019-fa89be7dd794" />
  <br>
  <em>Slika 1: Model UBA sustava (Izvor: generirano s UI alatom gemini.google.com)</em>
</p>

<br>


## Anomalije i strojno učenje

Anomalije u kontekstu User Behaviour Analytics sustava definiraju se kao ponašanja koja značajno odstupaju od uobičajenih obrazaca aktivnosti korisnika. Takva odstupanja ne moraju uvijek nužno predstavljati zlonamjernu aktivnost, ali često ukazuju na povećani sigurnosni rizik, osobito ako se pojavljuju učestalo ili u kombinaciji s drugim neuobičajenim događajima [2].

U suvremenim UBA rješenjima sve se češće primjenjuju tehnike strojnog učenja kako bi se automatizirala detekcija anomalija. Modeli strojnog učenja treniraju se na povijesnim podacima kako bi naučili normalne obrasce ponašanja korisnika te prepoznali odstupanja bez potrebe za unaprijed definiranim pravilima. Posebno su zastupljene nenadzirane metode učenja, budući da označeni podaci o sigurnosnim incidentima često nisu dostupni [6].

U okviru ovog projekta strojno učenje nije implementirano, već je primijenjen jednostavniji pristup temeljen na pragovima i ponašajnim pravilima. Takav pristup omogućuje jasnu interpretaciju rezultata i lakše razumijevanje procesa detekcije anomalija, što je osobito prikladno u edukativnom i demonstracijskom kontekstu.

---

## Virtualno okruženje

Za potrebe implementacije i evaluacije User Behaviour Analytics sustava korišteno je virtualno okruženje temeljeno na dvije odvojene virtualne mašine. Takav pristup omogućuje jasnu razdvojenost između poslužiteljskog dijela sustava i klijentskih aktivnosti, čime se vjernije simulira stvarno mrežno okruženje kakvo se može pronaći u organizacijama [7].

Prva virtualna mašina korištena je kao serversko okruženje, na kojem je pokrenuta ciljana aplikacija zajedno sa sustavima za prikupljanje metrika i nadzor sigurnosnih događaja. U tom okruženju generiraju se zapisi i metrike koji opisuju ponašanje korisnika te omogućuju analizu sigurnosno relevantnih događaja.

Druga virtualna mašina korištena je za simulaciju klijentskih aktivnosti. Na njoj su izvođene kontrolirane simulacije normalnog i anomalnog korisničkog ponašanja, čime je generiran realističan promet prema serverskom sustavu bez ugrožavanja njegove stabilnosti. Korištenjem ovakvog virtualnog okruženja omogućena je ponovljivost testiranja i jasna evaluacija učinkovitosti UBA mehanizama u detekciji neuobičajenog ponašanja.


