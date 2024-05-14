| Opis danych     | OPLS_OLD_original       | OPLS_OLD_new    | OPLS_NEW   | CHARMM |
|-----------------|-----------------|--------------|-------------|-----------|
| Liczba cząsteczek     | 162        | 162     | 512    | 500  | 
| Temperatura (K)   | 298,15        | 298,15     | 298,15    | 303,15  |
| Gęstość  (kg/m^3)   | 690.031        | 736.544      | 768.962    | 747.693  | 
| Entalpia swobodna hydratacji (kcal/mol)     | 18,51259454 (stara wartosc, obliczana ponownie)        | Dane 4,2 (tworzy sie)    | 27,03467998   | 16,19421346  | 
| Dyfuzja translacyjna  (1e-5 cm^2/s)    | 0.7169        | 0.4102     | 0.2845    | 0.5224  | 

**Etapy Obliczeń:
Tworzenie Boxa:
Rozpoczęliśmy od utworzenia symulacyjnego boxa zawierającego układ molekularny. W tym etapie określiliśmy wymiary boxa oraz ustawiliśmy odpowiednie warunki graniczne.

Równowaga Elektrostatyczna (EM):
Następnie przeprowadziliśmy równowagę elektrostatyczną (EM), w której zamroziliśmy pozycje atomów i minimalizowaliśmy energię potencjalną układu, usuwając ewentualne niestabilności strukturalne.

Równowaga Izotermiczna-Izochoryczna (NVT):
Po równowadze elektrostatycznej, przeprowadziliśmy równowagę izotermiczną-izochoryczną (NVT), kontrolując temperaturę układu poprzez oddziaływanie z termalnymi połaczeniami zewnętrznymi.

Równowaga Izotermiczna-Izobaryczna (NPT):
Następnie przeszliśmy do równowagi izotermicznej-izobarycznej (NPT), w której kontrolowaliśmy temperaturę i ciśnienie układu, umożliwiając dostosowanie objętości boxa do osiągnięcia stabilnego stanu.

Produkcja Dynamiki Molekularnej (MD):
Ostatecznie przeprowadziliśmy produkcję dynamiki molekularnej (MD), w której zarejestrowaliśmy trajektorię układu w czasie, aby zbadać zachowanie molekularne pod wpływem sił międzycząsteczkowych.
