Zadanie
V tomto zadaní je vašou úlohou urobiť kompletný proces spracovania dát a vytvorenia modelu. Najskôr dataset analyzujte a následne vykonajte predspracovanie. Na základe povahy datasetu si zvoľte 5 vhodných algoritmov strojového učenia a odôvodnite, prečo boli vybrané. Modely natrénujte, porovnajte pomocou vhodných metrík a krížovej validácie a vyhodnoťte výsledky na testovacej vzorke. Na záver interpretujte modely – vysvetlite, ktoré vlastnosti dát boli dôležité, kde modely robili chyby a ktorý algoritmus bol najvhodnejší a prečo.

 

Odovzdajte report a jupyter notebook.

 

Report bude obsahovať podrobný popis všetkých krokov vykonaných v tomto zadaní. Použite One-column IEEE journal article šablónu (jednostĺpcová). Pdf uložte s názvom: "Testovanie_Priezvisko.pdf"

 

Jupyter notebook má obsahovať kód, komentáre a byť reprodukovateľný. Názov: "Priezvisko.ipynb"



Dataset: Covertype - UCI Machine Learning Repository(https://archive.ics.uci.edu/dataset/31/covertype)

this data is initial it was changed later but may be useful to show the progress(
8 quantitive:


Validating model: XGBoost...
Completed in 7.77s. Average F1 (Weighted): 0.8570
Validating model: SGD Classifier...
Completed in 2.19s. Average F1 (Weighted): 0.6186
Validating model: Gaussian NB...
Completed in 0.36s. Average F1 (Weighted): 0.0899
Validating model: Extra Trees...
Completed in 8.25s. Average F1 (Weighted): 0.9204

--- Cross-Validation Complete ---
Average F1 (Weighted) scores of the models:
                F1_Weighted_CV
Extra Trees           0.920378
XGBoost               0.857025
SGD Classifier        0.618639
Gaussian NB           0.089936

-2 binary:

Validating model: Random Forest...
Completed in 9.43s. Average F1 (Weighted): 0.9131
Validating model: XGBoost...
Completed in 9.12s. Average F1 (Weighted): 0.8579
Validating model: SGD Classifier...
Completed in 3.32s. Average F1 (Weighted): 0.6340
Validating model: Gaussian NB...
Completed in 1.44s. Average F1 (Weighted): 0.1249
Validating model: Extra Trees...
Completed in 8.00s. Average F1 (Weighted): 0.9207

--- Cross-Validation Complete ---
Average F1 (Weighted) scores of the models:
                F1_Weighted_CV
Extra Trees           0.920721
Random Forest         0.913099
XGBoost               0.857912
SGD Classifier        0.633965
Gaussian NB           0.124930

10 quantitive(initial):


Validating model: XGBoost...
Completed in 9.41s. Average F1 (Weighted): 0.8570
Validating model: SGD Classifier...
Completed in 3.53s. Average F1 (Weighted): 0.6295
Validating model: Gaussian NB...
Completed in 1.74s. Average F1 (Weighted): 0.0904
Validating model: Extra Trees...
Completed in 8.40s. Average F1 (Weighted): 0.9204

--- Cross-Validation Complete ---
Average F1 (Weighted) scores of the models:
                F1_Weighted_CV
Extra Trees           0.920378
XGBoost               0.857025
SGD Classifier        0.629518
Gaussian NB           0.090378)

now this is the final result:

Validating model: KNN (K=5)...
Completed in 7.56s. Average F1 (Weighted): 0.8756
Validating model: XGBoost...
Completed in 7.46s. Average F1 (Weighted): 0.8579
Validating model: SGD Classifier...
Completed in 2.18s. Average F1 (Weighted): 0.6340
Validating model: Gaussian NB...
Completed in 0.44s. Average F1 (Weighted): 0.1249
Validating model: Extra Trees...
Completed in 7.15s. Average F1 (Weighted): 0.9207

--- Cross-Validation Complete ---
Average F1 (Weighted) scores of the models:
                F1_Weighted_CV
Extra Trees           0.920721
KNN (K=5)             0.875583
XGBoost               0.857912
SGD Classifier        0.633965
Gaussian NB           0.124930



--- Starting Final Evaluation on the Test Set ---
The best model from CV is: Extra Trees
Training the final model Extra Trees on the entire training set...
Model trained in 9.82s.
Performing prediction on the test set...

--- Classification Report (Test Set) ---
              precision    recall  f1-score   support

           0       0.97      0.96      0.96     42368
           1       0.96      0.98      0.97     56661
           2       0.95      0.97      0.96      7151
           3       0.91      0.88      0.89       549
           4       0.95      0.85      0.89      1899
           5       0.95      0.91      0.93      3473
           6       0.97      0.96      0.97      4102

    accuracy                           0.96    116203
   macro avg       0.95      0.93      0.94    116203
weighted avg       0.96      0.96      0.96    116203


Overall metrics on the test set:
Balanced Accuracy: 0.9282
F1 Score (Weighted): 0.9633

Generating Feature Importance for Extra Trees...

Top 15 most important features:
                                      feature  importance
0                            scale__Elevation    0.196498
5      scale__Horizontal_Distance_To_Roadways    0.107765
7   scale__Horizontal_Distance_To_Fire_Points    0.093232
3     scale__Horizontal_Distance_To_Hydrology    0.065985
1                               scale__Aspect    0.058890
4       scale__Vertical_Distance_To_Hydrology    0.052559
6                        scale__Hillshade_9am    0.050584
2                                scale__Slope    0.042398
49                remainder__Wilderness_Area3    0.037962
18                     remainder__Soil_Type10    0.032868
8                 remainder__Wilderness_Area1    0.032543
11                      remainder__Soil_Type3    0.029990
46                     remainder__Soil_Type38    0.025002
47                     remainder__Soil_Type39    0.022670
12                      remainder__Soil_Type4    0.015431