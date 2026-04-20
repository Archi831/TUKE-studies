V rámci tohto zadania budete testovať hyperparametre neurónových sietí (NS). Vaším cieľom je systematicky,
kontrolovane a reprodukovateľne zistiť, aká konfigurácia siete dosahuje najlepšie výsledky a prečo. Každý experiment
musí byť navrhnutý tak, aby bolo možné jednoznačne interpretovať vplyv testovaného hyperparametra.

Výber datasetu

Nájdite dataset, ktorý je dostatočne zložitý (aby rozdiely medzi modelmi boli merateľné) a má dostatočný počet
vzoriek (odporúčané: min. tisíce vzoriek). Môžete použiť dataset z minulého semestra (nemusíte).

Práca s datasetom

Pokiaľ dataset nemá defaultné rozdelenie, rozdeľte ho na train/validation/test. Validation množina slúži výhradne
na ladenie hyperparametrov. Test množina sa nesmie použiť počas navrhu modelu ani pri ladení hyperparametrov.
EDA vykonajte na tréningových (prípadne train+validation) dátach. Zahrňte základné štatistické charakteristiky a
vizualizácie (pandas, matplotlib, seaborn) a identifikujte vlastnosti datasetu, ktore môžu ovplyvniť učenie modelu.

Baseline model

Pred použitím neurónových sietí vytvorte baseline model, ktorý umožní objektívne porovnanie výsledkov. Baseline
musí byť adekvatny typu ulohy (napr. Logistic Regression alebo Random Forest pre klasifikaciu, Linear Regression
pre regresiu) a musí byť trénovaný a vyhodnotený na rovnakom rozdelení dát a rovnakými metrikami ako neurónové
siete.

Hodnotenie modelov

Pre všetky experimenty používajte konzistentné metriky. Uveď te explicitne, ktorá metrika slúži na výber najlepšieho
modelu. Každý experiment musí byť opakovaný minimálne 3x s rôznymi seedmi. Výsledky reportujte ako priemer a
smerodajnú odchýlku.

Testovanie rôznych topológií
Vytvorte 5 rôznych modelov s odlišnými topológiami (rôzny počet vrstiev a neurónov). Ostatné hyperparametre
(optimalizátor, learning rate, batch size) musia zostať konštantné, aby bolo možné izolovať vplyv topológie. De-
monštrujte underfitting a overfitting.

Testovanie rôznych optimalizátorov

Na najlepšiu topológiu aplikujte minimalne 3 optimalizatory. Porovnajte ich z hľadiska rýchlosti konvergencie (počet
epoch aj reálny čas) a stability tréningu (oscilácie, divergencia, plynulosť učenia).

Testovanie learning rate
Pre najlepšie nastavenie (topológia + optimalizátor) experimentujte s minimálne 5 hodnotami learning rate. Sledujte
stabilitu tréningu, rýchlosť učenia a kvalitu výsledného modelu. Vysvetlite pozorované správanie.

Testovanie aktivačných funkcií

Pre najlepšie nastavenie (topologia + optimalizator + learning rate) otestujte minimalne 5 aktivačných funkcií. V
krátkosti popíšte všetky (okrem sigmoidálnej) použité funkcie. Analyzujte vplyv na konvergenciu, stabilitu a výkon.

Regularizácia

Pre najlepšie nastavenie (topologia + optimalizator + learning rate + aktivačná funkcia) otestujte dropout a L2
regularizáciu. Vyhodnoťte ich vplyv na generalizáciu modelu a redukciu overfittingu.

Reprodukovateľnosť a tréning
Každý experiment musí byť reprodukovateľný. Nastavte random seed a zabezpečte konzistentné správanie tréningu.
Použite early stopping na základe validačnej metriky.

Odovzdávka - programovacia časť
. Python skript: Testovanie_Priezvisko.py
· všetky experimenty musia byť implementované reprodukovateľne (seed, rovnaké rozdelenie dát)

Odovzdávka - report
· Podrobný súhrn všetkých vykonaných experimentov s uvedením použitých parametrov a dosiahnutých výsledkov
(tabuľky sú povinné)
· Vizualizácie (napr. priebeh učenia, konfúzna matica) pre vybrané experimenty
· Diskusia o zisteniach - vysvetlenie, prečo jednotlivé nastavenia viedli k daným výsledkom
· Jednoznačná definícia najlepšieho modelu (na základe validačnej metriky) a jeho finálne vyhodnotenie na test
množine

· Uveďte všetky detaily potrebné na reprodukciu (architektúra, hyperparametre, seedy, použité knižnice)
· Použite One-column IEEE journal article šablónu (jednostĺpcová). Pdf uložte s názvom: Testovanie_Priezvisko.pdf