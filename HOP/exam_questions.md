# Okruh 1 : Základné pojmy a definície

### 1. Komponent, Kandidát a Priestor kandidátov

-   **Component (Komponent):** Najmenšia jednotka alebo „stavebný blok“ použitý na konštrukciu potenciálneho riešenia. Napríklad v grafovom probléme môže byť komponentom vrchol alebo hrana.
    
-   **Candidate (Kandidát):** Špecifická konfigurácia alebo „bod“ tvorený súborom komponentov. Predstavuje jednu možnú odpoveď v rámci priestoru vyhľadávania. Formálne s∈S.
    
-   **Candidate Space (Priestor kandidátov):** Množina S všetkých možných kandidátov, ktoré možno vytvoriť z daných komponentov problému. Jej veľkosť ∣S∣ určuje náročnosť úplného prehľadávania (exhaustive search).
    

### 2. Podmienky a Kvalita riešenia

-   **Conditions (Podmienky):** Logické obmedzenia, ktoré musí kandidát spĺňať, aby bol považovaný za „platného“ alebo „prípustného“. Tieto definujú **Rozhodovacie problémy**.
    
-   **Quality (Kvalita):** Hodnota priradená kandidátovi účelovou funkciou f(s). Meria, aký „dobrý“ je kandidát v porovnaní s ostatnými. Toto definuje **Optimalizačné problémy**.
    
-   **Combined (Kombinované):** Pri **Kombinovaných problémoch** potrebujete kandidáta, ktorý spĺňa všetky podmienky _a zároveň_ maximalizuje/minimalizuje kvalitu.
    

### 3. Problém, Model, Riešenie a Výsledok

-   **Problem (Problém):** Reálna výzva alebo úloha (napr. „Dodávka musí navštíviť všetkých zákazníkov“).
    
-   **Model:** Formálna/matematická abstrakcia problému (napr. Problém obchodného cestujúceho na grafe G=(V,E)).
    
-   **Solution (Riešenie):** Kandidát v rámci modelu, ktorý spĺňa všetky požiadavky.
    
-   **Result (Výsledok):** Praktická aplikácia riešenia späť do reálneho sveta (napr. skutočné GPS súradnice a trasa, ktorú vodič sleduje).
    

### 4. Heuristiky a Benchmarky

-   **Heuristics (Heuristiky):** Používajú sa na usmernenie prehľadávania priestorom S, keď je priestor príliš veľký na systematické prehľadávanie. Uprednostňujú „sľubné“ oblasti priestoru.
    
-   **Benchmarks (Benchmarky):** Štandardizované sady inštancií problémov (napr. TSPLIB pre obchodného cestujúceho), ktoré sa používajú na porovnanie výkonu, rýchlosti a presnosti rôznych heuristík.
    

### 5. Čo je Heuristika?

**Heuristika** je „zlaté pravidlo“ alebo stratégia, ktorá poskytuje praktický spôsob, ako nájsť riešenie.

-   **Goal (Cieľ):** Nájsť „dostatočne dobré“ riešenie v rozumnom časovom rámci. Nezaručuje nájdenie globálneho optima, ale vyhýba sa exponenciálnej časovej zložitosti úplného prehľadávania.
    

### 6. Príklad: Problém Sudoku

-   **Problem (Problém):** Vyplňte mriežku 9x9 tak, aby každý riadok, stĺpec a podmierežka 3x3 obsahovali číslice 1–9.
    
-   **Components (Komponenty):** Jednotlivé bunky a číslice {1,2,…,9}.
    
-   **Candidate (Kandidát):** Akákoľvek plne vyplnená mriežka 9x9.
    
-   **Candidate Space (Priestor kandidátov):** Všetky možné spôsoby vyplnenia mriežky (celkovo 981 kombinácií).
    

### 7. Problém vs. Inštancia & Kandidát vs. Riešenie

-   **Problem vs. Instance (Problém vs. Inštancia):** **Problém** je všeobecná trieda (napr. SAT). **Inštancia** je konkrétny prípad s fixnými údajmi (napr. konkrétna formula Φ).
    
-   **Candidate vs. Solution (Kandidát vs. Riešenie):** **Kandidát** je akýkoľvek bod v priestore vyhľadávania S (aj neprípustný). **Riešenie** je kandidát, ktorý spĺňa všetky obmedzenia/podmienky problému.
    

### 8. General Problem Solver (GPS)

-   **GPS:** Raný program umelej inteligencie (Newell & Simon, 1959) navrhnutý na riešenie akéhokoľvek problému, ktorý možno modelovať ako množinu stavov.
    
-   **Usage (Použitie):** Využíva **Analýzu prostriedkov a cieľov (Means-Ends Analysis)**. Porovnáva aktuálny stav s cieľovým stavom, identifikuje rozdiely a aplikuje operátory (akcie) na zmenšenie týchto rozdielov vytváraním podcieľov.
    

### 9. Príklady obmedzení a kvality

-   **Conditions only (Len podmienky - Rozhodovacie):** **Sudoku** alebo **SAT**. Stačí nájsť _akúkoľvek_ platnú konfiguráciu, ktorá spĺňa pravidlá.
    
-   **Quality only (Len kvalita - Optimalizačné):** **Aproximácia kriviek / Regresia**. Neexistujú „nelegálne“ čiary, ale niektoré pasujú k dátovým bodom lepšie ako iné (minimalizácia chyby).
    
-   **Both (Oboje - Kombinované):** **Problém batoha**. Predmety nesmú prekročiť váhový limit (Podmienka) A ZÁROVEŇ chcete maximalizovať celkovú hodnotu (Kvalita).
    

### 10. Štruktúra problému (Pohľad riešenia)

Z pohľadu riešenia sa problém skladá z:

1.  **Search Space (S):** Množina všetkých možných konfigurácií.
    
2.  **Feasibility Constraints:** Logika, ktorá filtruje S na platné riešenia.
    
3.  **Objective Function (f):** Mapovanie f:S→R, ktoré nám umožňuje porovnávať kandidátov.
    
4.  **Neighborhood Structure (N):** Definuje, ako sa môžeme počas vyhľadávania presunúť od jedného kandidáta k druhému.


----------
# Okruh 2: Prototypové problémy a klasifikácia

### 1. Farbenie grafov (Graph Coloring - GCP)

-   **Typ problému:** Model pre **kombinované/rozhodovacie problémy** (hľadanie prípustného k-farbenia).
    
-   **Inštancia:** Daný je graf G=(V,E) a počet farieb k.
    
-   **Úloha:** Priradiť každému vrcholu v∈V farbu tak, aby žiadne dva susedné vrcholy nemali rovnakú farbu.
    
-   **Typy:** * _Rozhodovací:_ Existuje k-farbenie?
    
    -   _Optimalizačný:_ Nájsť chromatické číslo χ(G) (minimálne k).
        

### 2. Problém splniteľnosti (SAT)

-   **Typ problému:** Prototypový **rozhodovací problém** (prvý dokázaný NP-úplný problém).
    
-   **Inštancia:** Booleovská formula v konjunktívnej normálnej forme (CNF) – množina klauzúl.
    
-   **Úloha:** Nájsť priradenie pravdivostných hodnôt premenným tak, aby bola celá formula pravdivá.
    
-   **Typy:** rozhodovací problém, optimalizačný problém (MAX-SAT – maximalizuj počet splnených klauzúl).
    

### 3. Problém obchodného cestujúceho (TSP)

-   **Typ problému:** Model pre **kombinované/optimalizačné problémy**.
    
-   **Inštancia:** Množina miest a matica vzdialeností (vážený graf).
    
-   **Úloha:** Nájsť Hamiltonovsky cyklus s minimálnou celkovou váhou (navštíviť každé mesto práve raz a vrátiť sa do štartu).
    
-   **Typy:** * _Symetrické TSP:_ Vzdialenosť A→B je rovnaká ako B→A.
    
    -   _Asymetrické TSP:_ Vzdialenosti sa líšia.
        
    -   _Euklidovské TSP:_ Miestami sú body v rovine.
        

### 4. Numerické vs. Kombinatorické problémy

-   **Numerické:** Premenné sú spojité (reálne čísla). Hľadáme hodnoty v spojitom priestore (napr. optimalizácia parametrov neurónovej siete, regresia).
    
-   **Kombinatorické:** Premenné sú diskrétne. Hľadáme objekt z konečnej (ale často obrovskej) množiny (napr. TSP, rozvrhovanie).
    

### 5. Rozhodovací problém a varianty

-   **Definícia:** Odpoveďou je "Áno" alebo "Nie" na otázku, či existuje riešenie spĺňajúce podmienky.
    
-   **Varianty:** rozhodovací (určiť ci existuje alebo nie), hľadací (nájdi jedno riešenie, alebo urči, že neexistuje).
    
-   **Príklad:** "Je tento graf zafarbiteľný 3 farbami?"
    

### 6. Optimalizačný problém a varianty

-   **Definícia:** Hľadáme riešenie ktore poskytuje optimalnu hodnotu účelovej funkcie.
    
-   **Varianty:** *hľadací* - nájsť riešenie s min/max hodnotou cieľovej funkcie; *ohodnocovací* - nájsť optimálnu hodnotu cieľovej funkcie
    
-   **Príklad:** "Aká je najkratšia cesta medzi týmito mestami?"
    

### 7. Kombinovaný problém

-   **Charakteristika:** Musí spĺňať tvrdé podmienky (validita) a zároveň optimalizovať kvalitu.
    
-   **Riešenie:** Musí patriť do množiny prípustných riešení Sfeasible​⊆S a zároveň dosahovať f(s)→opt.
    

### 8. Charakteristiky kandidáta (Rozhodovacie vs. Optimalizačné)

-   **Rozhodovacie:** Kandidát je buď validný (riešenie) alebo nevalidný. Kvalita nás nezaujíma.
    
-   **Optimalizačné:** Každý kandidát má priradenú hodnotu kvality, čo umožňuje porovnávanie dvoch kandidátov (lepšie/horšie).
    

### 9. Odvodenie veľkosti SAT

-   **Veľkosť inštancie:** n premenných, m klauzúl.
    
-   **Úplné priradenie:** 2n (každá premenná má 2 stavy).
    
-   **Parciálne priradenie:** 3n (stavy: True, False, Unassigned).
    

### 10. Odvodenie veľkosti TSP

-   **Veľkosť inštancie:** n miest, matica n×n.
    
-   **Priestor kandidátov:** (n−1)! pre fixný štartovací bod (v nesymetrickom prípade). V symetrickom prípade (n−1)!/2.
    

### 11. Odvodenie veľkosti Farbenia grafov

-   **Veľkosť inštancie:** n vrcholov, m hrán.
    
-   **Priestor kandidátov:** kn, kde k je počet dostupných farieb (každý z n vrcholov môže mať jednu z k farieb).

----------
# Okruh 3: Paradigmy prehľadávania a DPLL

### 1. Perturbačné vs. Konštrukčné prehľadávanie

-   **Konštrukčné:** Začínaš s prázdnym kandidátom a postupne pridávaš komponenty (napr. priraďuješ hodnoty premenným v SAT jednu po druhej), kým nemáš kompletného kandidáta.
    
-   **Perturbačné:** Začínaš s „úplným“ kandidátom (všetky komponenty sú prítomné) a následne ho modifikuješ (napr. zmeníš hodnotu jednej premennej v SAT – "flip").
    
-   **Kombinácia:** Najčastejšie sa používa **greedy konštrukcia** na vytvorenie počiatočného bodu, po ktorej nasleduje **perturbačné lokálne prehľadávanie** na jeho vylepšenie.
    

### 2. Jednotkový literál a orezávanie v DPLL

-   **Jednotkový literál (Unit Clause):** Ak klauzula obsahuje iba jeden nepriradený literál, musí byť splnený (true), inak by formula nebola splniteľná. To vynucuje hodnotu premennej.
    
-   **Orezávanie (Pruning):** Ak čiastočné priradenie vedie k prázdnej klauzule (kontradikcia), celá táto vetva v strome prehľadávania sa „odreže“ a algoritmus sa vráti späť (backtrack).
    
-   **Ukončenie:** Algoritmus končí úspechom (všetky klauzuly zmizli – formula je SAT) alebo vyčerpaním všetkých možností (UNSAT).
    

### 3. Základná štruktúra riešenia prehľadávaním

1.  **Inicializácia:** Nastavenie počiatočného stavu (prázdny kandidát alebo náhodný úplný kandidát).
    
2.  **Výber (Selection):** Výber komponentu alebo smeru pohybu (heuristika).
    
3.  **Transformácia:** Aplikácia operátora (pridanie komponentu alebo zmena existujúceho).
    
4.  **Evaluácia:** Vyhodnotenie kvality alebo podmienok.
    
5.  **Terminácia:** Kontrola, či sme našli riešenie alebo splnili limit.
    

-   **Rozdiel:** Algoritmy sa líšia v tom, ako robia krok 2 (Selection) – napr. náhodne vs. podľa skóre.
    

### 4. Systematické vs. Lokálne prehľadávanie

-   **Systematické:** Prechádza priestor tak, aby zaručene našlo riešenie (ak existuje). Je **úplné**. (Príklad: DPLL, Backtracking).
    
-   **Lokálne:** Pohybuje sa v okolí aktuálneho kandidáta. Nie je garantované, že prejde celý priestor. Je **neúplné**. (Príklad: Hill Climbing).
    
-   **Kombinácia:** Napr. systematické prehľadávanie na vyššej úrovni a lokálne prehľadávanie na riešenie sub-problémov.
    

### 5. Úplné a konštrukčné algoritmy

-   **Výhody:** Zaručujú nájdenie riešenia alebo dôkaz neexistencie (UNSAT).
    
-   **Nevýhody:** Časová zložitosť – v najhoršom prípade exponenciálna.
    
-   **Výber:** Vyberáme ich vtedy, keď je priestor kandidátov relatívne malý alebo potrebujeme 100 % istotu o výsledku.
    

### 6. Úplné vs. Neúplné algoritmy

-   **Úplné:** Nájdu riešenie vždy, ale sú pomalé (DPLL).
    
-   **Neúplné (Heuristické):** Sú rýchle a zvládnu obrovské inštancie, ale môžu sa zaseknúť v lokálnom optime a riešenie nenájsť (WalkSAT).
    
-   **Kedy ktorý:** Na malé, kritické úlohy Úplné. Na obrovské priemyselné problémy Neúplné.
    

### 7. Lokálne + Perturbačné/Konštrukčné

-   **Lokálne + Perturbačné:** Štandardné lokálne prehľadávanie. Máš celé riešenie a robíš v ňom malé zmeny (napr. 2-opt v TSP).
    
-   **Lokálne + Konštrukčné:** Menej časté, napr. "Iterated Greedy", kde časť riešenia rozbiješ (de-construction) a znova ho greedy dostaviaš.
    

### 8. Systematické + Perturbačné/Konštrukčné

-   **Systematické + Konštrukčné:** Klasický Backtracking/DPLL. Buduješ strom možností systematicky.
    
-   **Systematické + Perturbačné:** Napr. algoritmy, ktoré systematicky prechádzajú všetky možné perturbácie (napr. všetky 1-flipy v SAT), aby našli globálne maximum.
    

### 9. Výberová heuristika v DPLL

-   Určuje, ktorý literál L sa vyberie na vetvenie (splitting), keď nie je žiadna jednotková klauzula.
    
-   **Cieľ:** Čo najrýchlejšie vyvolať konflikt (kontradikciu) a orezať strom.
    
-   **Typy:**
    
    -   **Statické:** Pevné poradie premenných.
        
    -   **Dynamické:** (napr. MOMS, DLIS) – vyberajú premenné, ktoré sa najčastejšie vyskytujú v krátkych klauzulách.
        

### 10. Popis DPLL pseudokódu

```
Input: množina klauzúl Φ
Output: pravdivostná hodnota (splniteľnosť)

(I, Φ) ← UNIT-RESOLUTION(Φ)
if Φ = {}, return true
if {} ∊ Φ, return false
choose a literal L from Φ
if DPLL(Φ ∪ {{L}}) = true, return true
if DPLL(Φ ∪ {{¬L}}) = true, return true
return false
```

1.  **UNIT-RESOLUTION(Φ):** Prvý krok je propagácia jednotkových literálov. To zjednoduší formulu pred samotným vetvením.
    
2.  **if Φ={}:** Ak po zjednodušení neostali žiadne klauzuly, formula je splnená.
    
3.  **if {}∈Φ:** Ak vznikla prázdna klauzula, nastal konflikt (vetva je nesplniteľná).
    
4.  **choose a literal L:** Heuristický výber premennej pre vetvenie.
    
5.  **DPLL(Φ∪{L}):** Rekurzívny pokus: predpokladáme, že L je True.
    
6.  **DPLL(Φ∪{¬L}):** Ak predošlá vetva zlyhala, skúsime opak (¬L je True).
    
7.  **return false:** Ak ani jedna vetva nevedie k úspechu, celá pod-formula je nesplniteľná.




----------
# Okruh 4: Lokálne prehľadávanie a štruktúra okolia

### 1. Okolie pri lokálnom prehľadávaní (N(s))

Okolie je funkcia N:S→P(S), ktorá každému kandidátovi s priradí podmnožinu kandidátov s′∈S, ktorí sú z s "dosiahnuteľní" jedným krokom.

-   **Definícia:** Zvyčajne pomocou modifikácie (operátora) alebo vzdialenosti.
    
-   **Ohraničenia:**
    
    -   **Výpočtové:** Okolie nesmie byť príliš veľké (inak je funkcia `step` pomalá).
        
    -   **Kvalitatívne:** Musí byť dostatočne bohaté, aby existovala cesta ku globálnemu optimu (prepojenosť grafu okolia).
        

### 2. Lokálne prehľadávanie a globálne riešenie

Lokálne prehľadávanie sa nepokúša prehľadávať celý priestor S systematicky, ale pohybuje sa z aktuálneho stavu do susedného stavu (iteratívne vylepšovanie).

-   **Globálne riešenie (s∗):** Najlepší prvok v celom S (f(s∗)≤f(s) pre všetky s∈S).
    
-   **Lokálne riešenie (s^):** Najlepší prvok vo svojom okolí (f(s^)≤f(s′) pre všetky s′∈N(s^)).
    
-   **Rozdiel:** Pri rozhodovacích problémoch je lokálne riešenie (ktoré nie je globálne) zvyčajne bezcenné. Pri optimalizačných úlohách môže byť lokálne maximum akceptovateľným suboptimálnym výsledkom.
    

### 3. Okolie na základe vzdialenosti

Definuje sa ako Nϵ​(s)={s′∈S∣d(s,s′)≤ϵ}.

-   **Funkcia vzdialenosti d(s,s′):** Musí spĺňať vlastnosti metriky (nezápornosť, symetria, trojuholníková nerovnosť).
    
-   **Príklady:** * **Hammingova vzdialenosť:** Počet bitov, v ktorých sa líšia dva reťazce (vhodné pre SAT).
    
    -   **Euklidovská vzdialenosť:** Pre numerické problémy v Rn.
        

### 4. Okolie na základe mapovania

Okolie je definované pomocou operátora modifikácie m:S→S. Teda N(s)={s′∈S∣s′=m(s)}.

-   **Príklad:** V TSP operátor **2-opt**, ktorý odstráni dve hrany a nahradí ich inými dvoma tak, aby vznikla nová cesta.
    
-   **Využitie:** Mapovanie umožňuje definovať okolie nezávisle od geometrickej vzdialenosti, čisto na základe logiky štruktúry problému.
    

### 5. Graf okolia (GN​)

Je orientovaný (alebo neorientovaný) graf, kde vrcholy sú kandidáti s∈S a hrany vedú tam, kde s′∈N(s).

-   **Symetria:** Ak s′∈N(s)⟺s∈N(s′).
    
-   **Stupeň vrcholu:** Počet susedov v okolí (veľkosť okolia).
    
-   **Regulárnosť:** Každý kandidát má rovnako veľké okolie.
    
-   **Dostupnosť:** Existencia cesty medzi ľubovoľnými si​,sj​.
    
-   **Priemer grafu:** Maximálna vzdialenosť medzi dvoma vrcholmi (určuje teoretický minimálny počet krokov k riešeniu).
    

### 6. Komponenty lokálneho prehľadávania

1.  **Init (inicializácia):** Vygeneruje počiatočného kandidáta s0​ (náhodne alebo heuristicky).
    
2.  **Step (krok):** Funkcia, ktorá vyberie si+1​∈N(si​).
    
3.  **Term (ukončenie):** Podmienka zastavenia (napr. nájdenie riešenia, limit na iterácie, stagnácia).
    
4.  **Memory (voliteľné):** Uchováva informácie o predošlých stavoch (napr. Tabu list).
    


### 7. Analýza pseudokódu (Rozhodovací problém)

```
input: π
output: s ∊ S |  ⃞
( s, m ) = init(π) 
while( not term( s, m ) )
	( s, m ) = step( s, m )
endwhile
if( valid(s) ) then
	return s
else
	return   ⃞
endif
```

Tento algoritmus sa používa pre **rozhodovacie problémy** (napr. SAT).

-   **Kroky:** Inicializácia, slučka `while` vykonáva kroky prehľadávania, kým nie je splnená podmienka ukončenia. Na konci skontroluje, či je aktuálny stav `valid` (splnená formula) a vráti ho, inak vráti prázdnu množinu/symbol chyby.
    

### 8. Analýza pseudokódu (Minimalizácia)

```
input: π
output: r ∊ S |  ⃞
( s, m ) = init(π)
r = s
while( not term( s, m ) )
	( s, m ) = step( s, m )
	if( f( s ) < f( r )  ) then
		r = s
	endif
endwhile
if( valid(r) ) then
	return r
else
	return   ⃞
endif
```

Tento algoritmus je pre **optimalizačný problém (minimalizáciu)**.

-   **Kroky:** Uchováva si doteraz najlepšie nájdené riešenie v premennej r.
    
-   **Logika:** `if( f(s) < f(r) )` zabezpečuje, že r sa aktualizuje len vtedy, ak nájdeme kandidáta s nižšou (lepšou) hodnotou účelovej funkcie.
    

### 9. Prehľadávacia trajektória

```
input: π
output: r ∊ S |  ⃞
( s, m ) = init(π)
r = s
while( not term( s, m ) )
	( s, m ) = step( s, m )
	if( f( s ) > f( r )  ) then
		r = s
	endif
endwhile
if( valid(r) ) then
	return r
else
	return   ⃞
endif
```

Trajektória je postupnosť navštívených kandidátov T=⟨s0​,s1​,s2​,…⟩.

-   **Závislosť:** Závisí od počiatočného bodu, definície okolia a stratégie výberu suseda (`step`).
    
-   **Neinformovaná stratégia:** Nepoužíva hodnotu účelovej funkcie na navigáciu. Príkladom je **Random Walk** (náhodná prechádzka), kde susedov vyberáme čisto náhodne bez ohľadu na to, či sa zlepšujeme.
    

### 10. Analýza pseudokódu (Maximalizácia)

Ide o **optimalizačný problém**, konkrétne **maximalizáciu**.

-   **Identifikácia:** Podmienka `if( f(s) > f(r) )` hovorí, že si chceme pamätať kandidáta s _vyššou_ hodnotou účelovej funkcie.
    
-   **Zmena na minimalizáciu:** Stačí zmeniť relačný operátor v podmienke na `if( f(s) < f(r) )`.


----------
# Okruh 5: Iteračné vylepšovanie (Hill Climbing)

### 1. Ohodnocovacia funkcia a jej použitie

Ohodnocovacia (alebo cieľová) funkcia f:S→R priraďuje každému kandidátovi s číselnú hodnotu, ktorá reprezentuje jeho kvalitu.

-   **Použitie:** V iteračnom vylepšovaní slúži na porovnanie aktuálneho kandidáta so susedmi v okolí N(s). Algoritmus sa posunie len vtedy, ak nájde suseda s lepšou hodnotou f(s).
    
-   **Definícia pre rozhodovací problém:** Často sa definuje ako počet porušených podmienok (cieľom je f(s)=0).
    
-   **Definícia pre optimalizačný problém:** Priamo hodnota, ktorú chceme minimalizovať (napr. dĺžka cesty) alebo maximalizovať (napr. zisk).
    

### 2. Informovaná vs. neinformovaná stratégia

-   **Informovaná (Greedy):** Využíva hodnotu f(s) na smerovanie prehľadávania. Vyberá susedov, ktorí zlepšujú stav.
    
    -   _Ukončenie:_ Keď v okolí neexistuje žiaden lepší sused (dosiahnutie lokálneho optima).
        
-   **Neinformovaná (napr. Random Walk):** Ignoruje kvalitu kandidátov pri rozhodovaní o pohybe.
    
    -   _Ukončenie:_ Zvyčajne po nájdení riešenia (validného kandidáta) alebo po dosiahnutí limitu na počet krokov.
        

### 3. Podmienky pre ohodnocovaciu funkciu

Pre efektívne iteračné vylepšovanie musí f(s) spĺňať:

1.  **Konzistentnosť s cieľom:** Ak je s riešením, f(s) musí nadobúdať extrémnu (alebo cieľovú) hodnotu.
    
2.  **Dostatočná granularita:** Musí poskytovať "gradient" (smer), aby algoritmus vedel rozlíšiť medzi dvoma neoptimálnymi kandidátmi a nestagnoval na plochom povrchu.
    

### 4. SAT vs. MAXSAT

-   **Štandardný SAT (rozhodovací):** f(s) je počet nesplnených klauzúl. Cieľ je binárny: nájsť s, kde f(s)=0.
    
-   **MAXSAT (optimalizačný):** f(s) je počet splnených klauzúl (alebo ich váha). Cieľom je nájsť s s čo najvyšším počtom splnených klauzúl, aj keď nie sú splnené všetky.
    

### 5. Funkcia `step` pre minimalizáciu

Funkcia `step` prechádza okolie N(s) a hľadá množinu vylepšujúcich susedov I(s)={s′∈N(s)∣f(s′)<f(s)}.

-   **Best Improvement:** Vyberie s′∈I(s), ktoré minimalizuje f(s′) (najlepší z okolia).
    
-   **First Improvement:** Vyberie prvého nájdeného suseda, pre ktorého platí f(s′)<f(s).
    

### 6. Funkcia `init` a ukončenie vylepšovania

-   **`init`:** Zvyčajne vygeneruje náhodný počiatočný bod v priestore S (Uniform Random Point - `urp()`).
    
-   **Ukončenie:** Algoritmus končí, keď je množina vylepšujúcich susedov prázdna (I(s)=∅).
    
-   **Dôsledky:** Algoritmus uviazne v **lokálnom optime**. Ak toto optimum nie je globálne, algoritmus nenašiel najlepšie možné riešenie.
    

### 7. Vysvetlenie pseudokódu

```
input: π
output: s ∊ S |  ⃞
s = urp()                      // 1. Inicializácia: náhodný štartovací bod
while( #I( s ) > 0 )           // 2. Kým existujú susedia, ktorí zlepšujú riešenie
    s = select( I( s ) )       // 3. Vyber jedného z nich (pivotné pravidlo)
endwhile
if( valid( s ) ) then          // 4. Po zastavení skontroluj validitu
    return s
else
    return  ⃞                 // 5. Ak sme v lokálnom optime a nie je validné, vráť chybu
endif

```

### 8. Trajektória prehľadávania

Trajektória je **striktne monotónna** – každým krokom sa hodnota f(s) zlepšuje.

-   **Jeden extrém:** Algoritmus vždy nájde globálne optimum.
    
-   **Viac extrémov:** Algoritmus skončí v lokálnom optime, do ktorého spadá "spádová oblasť" počiatočného bodu `urp()`.
    

### 9. Uviaznutie v lokálnom optime

Je spôsobené **greedy povahou** algoritmu, ktorý nepovoľuje zhoršenie stavu ani pohyb po "rovine" (plateau).

-   **Vplyv:** Ak je priestor členitý, šanca na nájdenie globálneho optima klesá, pretože algoritmus nedokáže prejsť cez "kopec" (horšie riešenia) do vedľajšieho, hlbšieho údolia.
    

### 10. Funkcia `step` pre maximalizáciu

Logika je analogická k minimalizácii, ale množina vylepšujúcich susedov je definovaná ako I(s)={s′∈N(s)∣f(s′)>f(s)}. Algoritmus hľadá susedov s **vyššou** hodnotou účelovej funkcie. Pri `select` sa vyberá kandidát, ktorý zvyšuje f(s).



Tento okruh je o tom, ako "prekabátiť" terén účelovej funkcie, keď sa tvoj algoritmus zasekne v lokálnom údolí (alebo na kopci). Tu sú odpovede pre **Okruh 6**.

----------

# Okruh 6: Únik z lokálnych extrémov

### 1. Príčina uviaznutia a akceptácia horšieho riešenia

-   **Príčina:** Iteračné vylepšovanie je striktne greedy. Ak v okolí N(s) neexistuje žiaden sused s′ taký, že f(s′)<f(s) (pri minimalizácii), algoritmus zastane.
    
-   **Akceptácia horšieho riešenia:** Dovoľuje algoritmu "vyjsť z údolia" tým, že občas prijme krok, ktorý kvalitu zhorší. To mu umožní prekonať bariéru a nájsť inú spádovú oblasť, ktorá môže viesť k lepšiemu globálnemu optimu.
    
-   **Príklad:** **Simulované žíhanie (Simulated Annealing)**.
    

### 2. Zakázané lokálne prehľadávanie (Tabu Search)

-   **Princíp:** Používa krátkodobú pamäť (**Tabu list**), kde ukladá nedávno navštívené stavy alebo operácie. Tieto sú na istý čas "zakázané", čím algoritmus núti skúmať nové oblasti a bráni cykleniu.
    
-   **Ašpiračné kritérium:** Pravidlo, ktoré dovolí vykonať zakázaný krok, ak je "mimoriadne dobrý" (napr. vedie k lepšiemu riešeniu, než je doterajšie globálne maximum).
    
-   **Dlhodobá pamäť:** Sleduje frekvenciu návštev oblastí. Ak je nejaká oblasť navštevovaná príliš často, algoritmus vynúti skok do nepreskúmanej časti priestoru (**diverzifikácia**).
    

### 3. Opakované reštarty

-   **Pomoc:** Ak uviazneme, proste "hodíme kockou" a začneme z nového náhodného bodu s=urp().
    
-   **Kedy a prečo:** Používa sa, keď je priestor kandidátov veľmi členitý s mnohými lokálnymi optimami. Pravdepodobnosť, že aspoň jeden z n reštartov trafí spádovú oblasť globálneho optima, rastie s počtom pokusov.
    

### 4. Použitie väčšieho okolia

-   **Pomoc:** Čím je okolie N(s) väčšie, tým menej lokálnych extrémov v priestore existuje (viac susedov zvyšuje šancu, že aspoň jeden bude lepší).
    
-   **Výhody:** Väčšia šanca nájsť globálne optimum v jednom behu.
    
-   **Nevýhody:** Výpočtová náročnosť. Prehľadať okolie veľkosti O(n3) trvá oveľa dlhšie než O(n).
    

### 5. Pivotné pravidlá

Určujú, ktorého suseda z I(s) (množina zlepšujúcich susedov) si vyberieme:

1.  **Best Improvement (Greedy):** Prehľadá celé okolie a vyberie absolútne najlepšieho suseda.
    
2.  **First Improvement:** Vyberie prvého suseda, ktorého nájde a ktorý zlepšuje f(s). Rýchlejšie iterácie, ale menej kvalitný smer.
    
3.  **Random Improvement:** Náhodne vyberie jedného zo zlepšujúcich susedov.
    

### 6. Prepínanie okolí a VND (Variable Neighborhood Descent)

-   **Princíp:** Ak sa zasekneme v lokálnom optime pre okolie N1​, skúsime hľadať v inom okolí N2​ (napr. zmeníme typ pohybu).
    
-   **VND:** Algoritmus má sadu okolí N1​,…,Nk​. Začína s N1​. Ak nájde zlepšenie, vráti sa k N1​. Ak nenájde zlepšenie v Ni​, skúsi Ni+1​.
    
-   **Koniec:** Keď je aktuálny stav lokálnym optimom pre **všetky** definované okolia N1​…Nk​.
    

### 7. Dlhý krok a Lin-Kernighan

-   **Dlhý krok:** Vykonanie série zmien naraz, čo zodpovedá skoku do vzdialenejšej časti priestoru.
    
-   **Výhody/Nevýhody:** Prekoná lokálne optimá, ale môže "preskočiť" dobré riešenia a je náročný na implementáciu.
    
-   **Lin-Kernighan (pre TSP):** Adaptívny algoritmus, ktorý mení k hrán v grafe (k-opt). Proces generovania končí, keď ďalšia výmena hrán už nemôže viesť k zlepšeniu alebo sa dosiahne limit hĺbky.
    

### 8. Randomizované a pravdepodobnostné vylepšovanie

-   **Spoločné:** Oba vnášajú do procesu náhodu, aby unikli z optima.
    
-   **Rozdiel:**
    
    -   **Randomizované:** S pevnou pravdepodobnosťou p urobí náhodný krok namiesto zlepšujúceho.
        
    -   **Pravdepodobnostné (SA):** Pravdepodobnosť prijatia horšieho kroku závisí od rozdielu kvality Δf a parametra "teploty" T.
        
-   **Zabránenie uviaznutiu:** Náhodný pohyb umožní "vyskočiť" z lokálneho extrému.
    

### 9. Dynamické lokálne prehľadávanie (DLS)

-   **Princíp:** Nemení kandidáta pomocou náhody, ale mení **tvar účelovej funkcie**.
    
-   **Strategia:** Ak algoritmus uviazne, identifikuje črty (features) aktuálneho lokálneho optima a priradí im **penalizáciu**.
    
-   **Aplikácia:** Funkcia sa zmení na f′(s)=f(s)+penalizaˊcia. Údolie sa "zasype", až kým prestane byť lokálnym optimom a algoritmus je vytlačený von.
    

### 10. Základné prístupy (Zhrnutie)

1.  **Opakované štarty:** Spustenie algoritmu z rôznych náhodných bodov.
    
2.  **Akceptácia horšieho riešenia:** Povolenie krokov, ktoré dočasne zhoršujú kvalitu.
    
3.  **Zmena okolia:** Použitie inej štruktúry susedstva pri uviaznutí.
    
4.  **Zmena ohodnocovacej funkcie:** Penalizácia nájdených lokálnych optím.
    
5.  **Použitie pamäte:** Zakázanie návratu do už navštívených stavov.



Tento okruh prechádza od klasickej teórie hier k umelej inteligencii v hrách a končí učením posilňovaním. Tu sú odpovede pre **Okruh 7**.

----------

# Okruh 7: Teória hier a učenie posilňovaním

### 1. Hry s nulovým vs. nenulovým súčtom

-   **Hry s nulovým súčtom (Zero-sum):** Čistý konflikt. To, čo jeden hráč získa, druhý musí stratiť. Súčet ziskov a strát je vždy konštantný (napr. šach, poker o peniaze).
    
-   **Hry s nenulovým súčtom:** Existuje možnosť, kde obaja hráči získajú (win-win) alebo obaja stratia (lose-lose). Súčet nie je fixný (napr. obchodovanie, väzňova dilema).
    

### 2. Kooperatívne vs. antagonistické hry

-   **Antagonistické:** Hráči idú ostro proti sebe, záujmy sú v priamom rozpore (typické pre hry s nulovým súčtom).
    
-   **Kooperatívne:** Hráči môžu komunikovať a uzatvárať záväzné dohody alebo koalície, aby maximalizovali spoločný zisk.
    

### 3. Nashova rovnováha

Je to stav v hre s dvoma alebo viacerými hráčmi, kde **žiaden hráč nemôže získať viac jednostrannou zmenou svojej stratégie**, ak ostatní hráči svoje stratégie nezmenia. V tomto bode je stratégia každého hráča optimálnou odpoveďou na stratégie ostatných.

### 4. Bodovacia funkcia (Heuristika) pri Minimax-e

Keďže strom hry (napr. šach) je príliš hlboký na úplné prehľadávanie, bodovacia funkcia odhaduje "výhodnosť" stavu pre daného hráča v listoch, ktoré nie sú koncovými stavmi hry.

-   **Účel:** Priradiť číselnú hodnotu (napr. +100 pre výhru, -100 pre prehru, 0 pre remízu), podľa ktorej sa algoritmus rozhoduje.
    

### 5. Princíp algoritmu Minimax

Algoritmus predpokladá, že obaja hráči hrajú optimálne.

1.  **MAX hráč:** Snaží sa maximalizovať bodové skóre.
    
2.  **MIN hráč:** Snaží sa minimalizovať bodové skóre (maximalizovať svoju výhodu). Algoritmus rekurzívne prechádza strom hry do určitej hĺbky a prebubláva hodnoty smerom nahor: v uzloch MAX vyberá maximum z potomkov, v uzloch MIN vyberá minimum.
    

### 6. Alfa-beta orezávanie (Pruning)

Je to optimalizácia Minimaxu, ktorá drasticky znižuje počet prehľadávaných uzlov bez zmeny výsledku.

-   **α:** Najlepšia (najvyššia) hodnota, ktorú má MAX hráč doteraz zaručenú.
    
-   **β:** Najlepšia (najnižšia) hodnota, ktorú má MIN hráč doteraz zaručenú.
    
-   **Princíp:** Ak v ktoromkoľvek bode zistíme, že α≥β, zvyšok tejto vetvy sa **oreže**, pretože vieme, že racionálny hráč by do tejto vetvy nikdy nevstúpil.
    

### 7. Interakcia Agent – Prostredie (RL)

Základom je uzavretá slučka (feedback loop):

1.  **Agent** pozoruje aktuálny **stav** (st​) prostredia.
    
2.  Na základe toho vykoná **akciu** (at​).
    
3.  **Prostredie** zareaguje: zmení stav na st+1​ a pošle agentovi **odmenu** (rt+1​).
    

### 8. Priebeh učenia v RL

Učenie prebieha metódou pokus-omyl. Agent si buduje tabuľku alebo funkciu (napr. Q-funkciu), ktorá mu hovorí, aká dobrá je daná akcia v danom stave. Cieľom je aktualizovať tieto hodnoty na základe získaných odmien tak, aby v budúcnosti agent volil akcie, ktoré vedú k najvyššiemu zisku.

### 9. Kumulatívna odmena

Definuje sa ako súčet všetkých budúcich odmien, ktoré agent získa od aktuálneho času t. Aby sme uprednostnili skoršie odmeny pred neskoršími, používa sa **discount factor** γ∈[0,1]:

$G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$

### 10. Nájdenie optimálnej politiky (π∗)

Politika π je predpis (mapovanie), ktorý hovorí agentovi, akú akciu má zvoliť v danom stave. Optimálna politika π∗ je taká, ktorá pre každý stav maximalizuje očakávanú kumulatívnu odmenu. Algoritmy (napr. Q-learning) ju hľadajú iteratívnym vylepšovaním odhadov hodnoty stavov a akcií.


----------
# Okruh 8: Optimalizácia mravčích kolónií (ACO)

### 1. Použitie feromónu v ACO

Feromón (τ) slúži ako **globálna zdieľaná pamäť** kolónie.

-   Mravce pri pohybe ukladajú feromón na hrany grafu.
    
-   Hrany s vyššou koncentráciou feromónu majú vyššiu pravdepodobnosť, že si ich vyberú ďalšie mravce.
    
-   Týmto spôsobom sa realizuje **pozitívna spätná väzba**, ktorá vedie kolóniu k objaveniu a ustáleniu sa na kvalitných riešeniach.
    

### 2. ACO pre problém obchodného cestujúceho (TSP)

Pri TSP mravce reprezentujú agentov, ktorí budujú riešenie (Hamiltonovskú kružnicu):

-   **Uzly grafu:** Mestá.
    
-   **Hrany:** Cesty medzi mestami, ktoré majú priradenú dĺžku (lokálna informácia) a hladinu feromónu (globálna informácia).
    
-   **Cieľ:** Mravce sa snažia prejsť všetky mestá a vrátiť sa do štartu tak, aby výsledná dĺžka bola minimálna. Cesty, ktoré sú súčasťou kratších trás, dostanú v update fáze viac feromónu.
    

### 3. Hľadanie najkratšej cesty

Hľadanie je založené na princípe, že mravce, ktoré nájdu kratšiu cestu, ju prejdú rýchlejšie (alebo za rovnaký čas vykonajú viac cyklov). V digitálnom modeli to simulujeme tak, že mravec po dokončení trasy pridá na použité hrany množstvo feromónu **nepriamo úmerné dĺžke trasy** (1/L). Čím je cesta kratšia, tým silnejšia je feromónová stopa.

### 4. Vlastnosti umelého mravca

-   **Pravdepodobnostný výber:** Nevyberá si cestu čisto greedy, ale na základe pravdepodobnosti.
    
-   **Pamäť:** Udržiava si zoznam už navštívených uzlov (Tabu list).
    
-   **Lokálne videnie:** Pozná vzdialenosť do susedných miest (heuristická informácia).
    
-   **Ukladanie feromónu:** Modifikuje prostredie po nájdení riešenia.
    

### 5. Model mravčieho sveta

Mravčí svet je modelovaný ako plne prepojený vážený graf G=(V,E).

-   **Vlastnosti:** * Na každej hrane (i,j) je hodnota τij​ (feromón) a ηij​ (viditeľnosť/heuristika).
    
    -   Svet je diskrétny a statický počas jednej iterácie (mravce sa hýbu po krokoch).
        

### 6. Výber smeru pohybu

Mravec k v uzle i si vyberá nasledujúci uzol j podľa pravdepodobnostného pravidla (Transition Rule):

Pijk​=∑l∈Jk​​[τil​]α⋅[ηil​]β[τij​]α⋅[ηij​]β​

Kde α ovplyvňuje váhu feromónu, β váhu heuristiky a Jk​ je množina povolených (nenavštívených) uzlov.

### 7. Statická vs. dynamická váha

-   **Statická váha (ηij​):** Heuristická informácia, zvyčajne prevrátená hodnota vzdialenosti (1/dij​). Počas behu algoritmu sa **nemení**. Vyjadruje lokálnu atraktivitu hrany.
    
-   **Dynamická váha (τij​):** Hladina feromónu. **Mení sa** v každej iterácii na základe úspešnosti mravcov. Vyjadruje globálnu skúsenosť kolónie.
    

### 8. Pamäť umelého mravca

Pamäť mravca obsahuje tzv. **Tabu list** (zoznam navštívených miest).

-   **Využitie:** Pri výbere smeru pohybu mravec filtruje susedné uzly tak, aby sa nepohyboval do miest, ktoré už navštívil. Tým je zaručené, že výsledná cesta bude Hamiltonovská (každé mesto práve raz).
    

### 9. Odparovanie feromónu (Evaporation)

Odparovanie slúži na **zabránenie predčasnej konvergencii** k lokálnemu optimu.

-   **Definícia:** τij​=(1−ρ)⋅τij​, kde ρ∈[0,1] je koeficient odparovania.
    
-   **Aplikácia:** Vykonáva sa v update fáze po tom, čo všetky mravce dokončia svoje cesty. Umožňuje kolónii "zabudnúť" staré, menej kvalitné cesty a uvoľniť priestor pre nové objavy.
    

### 10. Vysvetlenie krokov pseudokódu


```Python
input: π (inštancia), max (max iterácií)
output: r ∊ S (najlepšie nájdené riešenie)

r = ⃞, g(r) = ∞            # Inicializácia globálneho optima (symbol prázdna a nekonečno)
i = 1
repeat
    initialize-ants()       # Vyčistenie pamäte mravcov, umiestnenie do štartovacích miest
    while ( not memory-full() )
        move-ants()         # Každý mravec si vyberie ďalší uzol podľa Transition Rule
        update-memory()     # Pridanie navštíveného uzla do Tabu listu
    endwhile
    s = shortest-path()     # Nájdenie najlepšieho riešenia v aktuálnej iterácii
    if ( g(s) < g(r) ) then
        r = s               # Aktualizácia globálneho rekordéra
    endif
    contributions()         # Výpočet feromónu, ktorý mravce pridajú na svoje trasy
    update()                # Aplikácia odparovania a pripočítanie nových príspevkov
    i = i + 1
until i > max
return r
```


----------
# Okruh 9: Algoritmus BFO

### 1. Rozdiely medzi cyklami (Chemotaxia, Reprodukcia, Disperzia)

Algoritmus je štruktúrovaný hierarchicky (vnorené cykly):

-   **Chemotaxia (vnútorný):** Zodpovedá za **lokálne prehľadávanie**. Baktéria sa pohybuje (swim/tumble) v smere gradientu kvality.
    
-   **Reprodukcia (stredný):** Zabezpečuje **konvergenciu**. Najlepšie baktérie sa duplikujú, čím sa populácia sústreďuje do sľubných oblastí.
    
-   **Disperzia (vonkajší):** Zabezpečuje **exploráciu** (únik z lokálnych optím). Náhodne premiestni časť populácie do úplne iných častí priestoru.
    

### 2. Reprodukcia: Definícia a účel

-   **Definícia:** Baktérie sa zoradia podľa ich "zdravia" (kumulatívna hodnota účelovej funkcie počas chemotaxie). Dolná polovica (najmenej fit) zanikne, horná polovica sa rozdelí na dve identické baktérie.
    
-   **Účel:** Simuluje evolučný tlak. Udržiava populáciu v dobrých oblastiach a zvyšuje priemernú kvalitu bez toho, aby sa zmenila veľkosť populácie.
    

### 3. Problémy, priestor a funkcia `step`

-   **Problémy:** Hlavne numerická optimalizácia v spojitom priestore (napr. hľadanie minima funkcie viacerých premenných).
    
-   **Priestor kandidátov:** Zvyčajne n-rozmerný spojitý priestor Rn.
    
-   **Funkcia `step`:** V BFO je to kombinácia náhodného otočenia (**tumble**) a posunu o dĺžku kroku C(i) v danom smere (**swim**). Ak sa kvalita zlepší, baktéria pokračuje v plávaní v rovnakom smere.
    

### 4. Priebeh priemernej kvality

-   **Chemotaxia:** Priemerná kvalita plynule rastie (baktérie sa hýbu smerom k lepším hodnotám).
    
-   **Reprodukcia:** Skokové zlepšenie (odstránením polovice zlých baktérií priemer okamžite stúpne).
    
-   **Disperzia:** Náhly pokles kvality (keďže baktérie sú vyhodené na náhodné miesta), ale je nevyhnutná pre objavenie globálneho optima.
    

### 5. Sociálne správanie

Definuje sa cez funkcie **atraktivity** a **repelencie**.

-   Baktérie pri pohybe vylučujú látky, ktoré priťahujú ostatné baktérie (zhlukovanie v dobrých oblastiach) a zároveň udržiavajú mierny odstup (prevencia pred úplným zhluknutím v jednom bode). To vytvára dynamiku, kde populácia kooperuje pri prehľadávaní.
    

### 6. Reprodukcia vs. Disperzia (Implementácia)

-   **Reprodukcia:** Implementovaná ako elitársky výber (sort a copy). Slúži na **exploatáciu** (vyťaženie známej oblasti).
    
-   **Disperzia (Elimination-Dispersal):** Implementovaná pomocou pravdepodobnosti ped​. Ak náhodné číslo <ped​, baktéria je "zabitá" a znovu inicializovaná na náhodnom mieste. Slúži na **globálnu exploráciu**.
    

### 7. Pohyb simulovanej baktérie

Pohyb sa rieši v **chemotaxickom cykle**. Pozostáva z:

1.  **Tumble:** Vygenerovanie náhodného smerového vektora.
    
2.  **Swim:** Posun v tomto smere.
    

-   **Význam:** Je to základný mechanizmus hľadania riešenia. Bez pohybu by algoritmus neprehľadával priestor, len náhodne vzorkoval.
    

### 8. Simulovaný vs. skutočný pohyb

-   **Realita:** Baktérie majú bičíky a plávajú v kvapaline konštantnou rýchlosťou, pričom menia dĺžku plávania podľa koncentrácie živín.
    
-   **Algoritmus:** Modeluje to diskrétnym krokom C(i). Ak je smer dobrý, robí ďalšie kroky. Implementácia v kóde: $x_{\text{new}} = x_{\text{old}} + C(i)\cdot \frac{\Delta}{\sqrt{\Delta^T \Delta}}$​, kde Δ je náhodný vektor.
    

### 9. Pamäť v BFO

**Áno, využíva sa.**

-   **Čo uchováva:** Kumulatívnu sumu hodnôt účelovej funkcie (Jhealth​) počas všetkých krokov chemotaxie.
    
-   **Kedy sa aktualizuje:** Po každom kroku v cykle chemotaxie.
    
-   **Prečo:** Bez tejto pamäte by sme pri reprodukcii nevedeli určiť, ktoré baktérie boli celkovo úspešné a ktoré len mali "šťastie" na náhodný počiatočný bod.
    

### 10. Dĺžka pohybu a ukončenie

-   **Dĺžka:** Určená parametrom C(i) (unit walk).
    
-   **Podmienky ukončenia plávania (Swim loop):**
    
    -   **Minimalizácia:** Ak f(snew​)≥f(sold​) (už sa nezlepšujeme).
        
    -   **Maximalizácia:** Ak f(snew​)≤f(sold​).
        
    -   Dosiahnutie fixného limitu počtu krokov plávania (Ns​).


----------
# Okruh 10: Algoritmus umelých včiel (ABC)

### 1. Úlohy včiel v algoritme ABC

Včely sa delia na tri kategórie podľa ich aktuálnej aktivity:

-   **Zamestnané včely (Employed bees):** Sú priradené ku konkrétnemu zdroju potravy (kandidátovi). Vyťažujú ho a hľadajú v jeho okolí lepšie riešenia.
    
-   **Pozorovateľky (Onlooker bees):** Čakajú v úli a na základe informácií od zamestnaných včiel si vyberajú sľubné zdroje, ktoré idú ďalej vyťažovať.
    
-   **Prieskumníčky (Scout bees):** Ak je zdroj potravy vyčerpaný (nedošlo k zlepšeniu po istý počet krokov), zamestnaná včela sa zmení na prieskumníčku a hľadá úplne nový, náhodný zdroj.
    

### 2. Základná štruktúra iterácií

Algoritmus prebieha v cykloch:

1.  **Inicializácia:** Vygenerovanie náhodných zdrojov potravy (populácia riešení).
    
2.  **Fáza zamestnaných včiel:** Každá včela modifikuje svoj priradený zdroj (lokálne prehľadávanie).
    
3.  **Fáza pozorovateliek:** Výber zdrojov na základe ich kvality (fitness) a ich ďalšie lokálne prehľadávanie.
    
4.  **Fáza prieskumníčok:** Identifikácia vyčerpaných zdrojov a ich nahradenie náhodnými.
    
5.  **Uloženie najlepšieho riešenia:** Aktualizácia globálneho maxima/minima.
    

### 3. Zmena roly včely

Rola včely je dynamická:

-   **Zamestnaná → Prieskumníčka:** Nastáva vtedy, keď sa hodnota zdroja nezlepšila počas vopred daného počtu iterácií (parameter `limit`). Zdroj sa považuje za lokálne optimum a včela ho opúšťa.
    
-   **Prieskumníčka → Zamestnaná:** Akonáhle prieskumníčka náhodne objaví nový zdroj potravy, stáva sa opäť zamestnanou včelou priradenou k tomuto zdroju.
    

### 4. Prostredie, včela a zdroj potravy

-   **Prostredie:** Modelované ako d-rozmerný priestor kandidátov S.
    
-   **Zdroj potravy (Food Source):** Zodpovedá **kandidátovi** (riešeniu) s∈S. Kvalita zdroja (množstvo nektáru) zodpovedá hodnote účelovej funkcie f(s).
    
-   **Včela:** Predstavuje **výpočtového agenta** (operátor), ktorý vykonáva zmeny na kandidátovi.
    

### 5. Vyťažovanie, opustenie a nájdenie zdroja

-   **Vyťažovanie:** Lokálne prehľadávanie v okolí aktuálneho riešenia (**Exploitácia**). Vedie k spresňovaniu riešenia.
    
-   **Opustenie:** Mechanizmus úniku z lokálneho optima. Ak sa riešenie nezlepšuje, zahodíme ho.
    
-   **Nájdenie nového zdroja:** Náhodný skok do nepreskúmanej časti priestoru (**Explorácia**). Zabezpečuje diverzitu populácie.
    

### 6. Vyťažovanie zdroja a výber suseda

Zamestnaná včela alebo pozorovateľka generuje nového kandidáta vi​ v okolí aktuálneho zdroja xi​ podľa vzťahu:

vij​=xij​+ϕij​(xij​−xkj​)

Kde xk​ je náhodne vybraný iný zdroj, j je náhodná dimenzia a ϕ je náhodné číslo v intervale [−1,1]. Týmto "posunom" smerom k (alebo od) iného zdroja včela skúma okolie.

### 7. Typy selekcie v ABC

-   **Pravdepodobnostná:** Pozorovateľky si vyberajú zdroje pomocou rulety – čím vyššie fitness, tým vyššia šanca na výber.
    
-   **Lačná (Greedy):** Pri vyťažovaní zdroja; včela si ponechá nového kandidáta vi​ len vtedy, ak je lepší ako pôvodný xi​.
    
-   **Náhodná:** Prieskumníčka generuje nový zdroj náhodne v celom povolenom priestore.
    

### 8. Exploatácia vs. Explorácia

-   **Exploatácia:** Sústredenie sa na známe sľubné oblasti. V ABC ju robia **zamestnané včely** a **pozorovateľky**. Nadmerná exploatácia vedie k uviaznutiu v lokálnom optime.
    
-   **Explorácia:** Prehľadávanie neznámych oblastí. V ABC ju robia **prieskumníčky**. Nadmerná explorácia sa podobá náhodnému prehľadávaniu a spomaľuje konvergenciu.
    

### 9. Výber zdroja podľa roly

-   **Zásobovačka (Zamestnaná):** Má fixný vzťah 1:1 k svojmu zdroju. Nevyberá si, ale vylepšuje ten, ktorý jej bol pridelený.
    
-   **Pozorovateľka:** Vyberá si na základe **pravdepodobnosti** (fitness-proportional selection). Implementované ako: Pi​=∑fitj​fiti​​.
    
-   **Prieskumníčka:** Hľadá náhodne, implementované ako nová inicializácia vektora v hraniciach [xmin​,xmax​].
    

### 10. Podiel včiel v populácii

-   **Podiel:** Štandardne je populácia rozdelená na **50 % zamestnaných včiel** a **50 % pozorovateliek**. Počet zdrojov potravy je rovný počtu zamestnaných včiel (SN).
    
-   **Zmena podielu:** Počet zamestnaných včiel a pozorovateliek ostáva počas behu algoritmu konštantný. Prieskumníčka je len dočasný stav zamestnanej včely; v každom cykle môže byť maximálne jedna (alebo malý počet) prieskumníčka, aby sa nenarušila stabilita prehľadávania.
