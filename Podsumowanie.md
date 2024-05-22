### Wyniki własnych obliczeń dla n-pentadekanu

| Opis danych     | OPLS_1996       | OPLS_2013   | OPLS_2022   | CHARMM_36 |
|-----------------|-----------------|--------------|-------------|-----------|
| Gęstość  (kg/m^3)   | 690.031        | 736.544      | 768.962    | 747.693  | 
| Entalpia Parowania (kcal/mol)     | 18,40026187        | 16,13039783    | 27,03467998   | 16,19421346  | 
| Dyfuzja translacyjna  (1e-5 cm^2/s)    | 0.7169        | 0.4102     | 0.2845    | 0.5224  | 

### Wartości Referencyjne dla Pentadekanu OPLS_2013
| Opis danych     | OPLS_1996 | OPLS_2013 | Reference/Wartość eksperymentalna |
|-----------------|-----------------|------------|-------------|
| Gęstość  (kg/m^3)   | 840 |  745  | 765 
| Entalpia Parowania (kcal/mol)     | 28.49  |   18.41 | 18.35    
| Dyfuzja translacyjna  (1e-5 cm^2/s)    | 4.77 |  4.57 |  4.13

### Wartości Referencyjne dla Pentadekanu CHARMM_36 w temp 298 K
| Opis danych     | CHARMM |
|-----------------|-----------------|
| Gęstość  (kg/m^3)   | 759.66   
| Entalpia Parowania (kcal/mol)     | 17.88   
| Dyfuzja translacyjna  (1e-5 cm^2/s)    | 5.71 

### Wersja Gromacs Z Publikacji 
    GROMACS v 4.5.5.
### Wersja Gromacs Własnych Obliczeń
    GROMACS v 2022.4
### Przebieg obliczeń symulacji molekularnej

1. **Tworzenie Boxa**:
   Rozpoczęliśmy od utworzenia symulacyjnego boxa zawierającego układ molekularny. W tym etapie określiliśmy wymiary boxa oraz ustawiliśmy odpowiednie warunki graniczne takie jak ilość cząsteczek i wykorzystanie odpowiedniego pola siłowego.

2. **Równowaga Elektrostatyczna (EM)**:
   Następnie przeprowadziliśmy równowagę elektrostatyczną (EM), w której zamroziliśmy pozycje atomów i minimalizowaliśmy energię potencjalną układu, usuwając ewentualne niestabilności strukturalne.

3. **Równowaga Izotermiczna-Izochoryczna (NVT)**:
   Po równowadze elektrostatycznej, przeprowadziliśmy równowagę izotermiczną-izochoryczną (NVT), kontrolując temperaturę układu poprzez oddziaływanie z termalnymi połaczeniami zewnętrznymi.

4. **Równowaga Izotermiczna-Izobaryczna (NPT)**:
   Następnie przeszliśmy do równowagi izotermicznej-izobarycznej (NPT), w której kontrolowaliśmy temperaturę i ciśnienie układu, umożliwiając dostosowanie objętości boxa do osiągnięcia stabilnego stanu.

5. **Produkcja Dynamiki Molekularnej (MD)**:
   Ostatecznie przeprowadziliśmy produkcję dynamiki molekularnej (MD), w której zarejestrowaliśmy trajektorię układu w czasie, aby zbadać zachowanie molekularne pod wpływem sił międzycząsteczkowych.

