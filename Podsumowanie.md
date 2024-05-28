### Parametry Symulacji

| Parametr               | OPLS_1996 | OPLS_2013 | OPLS_2022 | CHARMM_36 |
|------------------------|-----------|-----------|-----------|-----------|
| Liczba cząsteczek      | 162      | 162      | 512      | 162      |
| Liczba kroków (nsteps) | 50000000  | 50000000    | 50000000    | 50000000   |  = 100ns
| Temperatura (K)        | 298,15       | 298,15       | 298,15       | 298,15       |

### Wartości Eksperymentalne i Symulacyjne

| Opis danych                   | Wartości eksperymentalne | OPLS_1996                | OPLS_2013               | OPLS_2022               | CHARMM_36              |
|-------------------------------|--------------------------|--------------------------|-------------------------|-------------------------|------------------------|
| Gęstość  (kg/m^3)             | 765                      | 690.031                  | 736.544                 | 768.962                 | 747.693                |
| Entalpia Parowania (kcal/mol) | 18.35                    | 18.40026187              | 16.13039783             | 27.03467998             | 16.19421346            |
| Dyfuzja translacyjna (cm²/µs) | 4.13 × 10<sup>-7</sup>   | 7.169 × 10<sup>-7</sup>  | 4.102 × 10<sup>-7</sup> | 2.845 × 10<sup>-7</sup> | 5.224 × 10<sup>-7</sup> |

### Wartości Referencyjne dla Pentadekanu OPLS_2013

| Opis danych                   | OPLS_1996                | OPLS_2013               | Wartość eksperymentalna/Referencyjna |
|-------------------------------|--------------------------|-------------------------|--------------------------------------|
| Gęstość  (kg/m^3)             | 840                      | 745                     | 765                                  |
| Entalpia Parowania (kcal/mol) | 28.49                    | 18.41                   | 18.35                                |
| Dyfuzja translacyjna (cm²/µs) | 4.77 × 10<sup>-7</sup>   | 4.57 × 10<sup>-7</sup>  | 4.13 × 10<sup>-7</sup>               |

### Wartości Referencyjne dla Pentadekanu CHARMM_36 w temp 298 K

| Opis danych                   | CHARMM                  |
|-------------------------------|-------------------------|
| Gęstość  (kg/m^3)             | 759.66                  |
| Entalpia Parowania (kcal/mol) | 17.88                   |
| Dyfuzja translacyjna (cm²/µs) | 5.71 × 10<sup>-7</sup>  |

### Wyniki własnych obliczeń dla n-dodekanu

| Opis danych                   | OPLS_1996               | OPLS_2013              | OPLS_2022              | CHARMM_36             |
|-------------------------------|-------------------------|------------------------|------------------------|-----------------------|
| Gęstość  (kg/m^3)             | 697.61                  | 697.751                | 534.676                | 729.296               |
| Entalpia Parowania (kcal/mol) | 12.90323413             | 12.89647475            | 20.6597433             | 13.07980533           |
| Dyfuzja translacyjna (cm²/µs) | 1.3423 × 10<sup>-6</sup>| 4.3902 × 10<sup>-6</sup>| 2.7648 × 10<sup>-6</sup>| 7.0291 × 10<sup>-6</sup> |

### Wyniki własnych obliczeń dla n-oktanu

| Opis danych                   | OPLS_1996               | OPLS_2013              | OPLS_2022              | CHARMM_36             |
|-------------------------------|-------------------------|------------------------|------------------------|-----------------------|
| Gęstość  (kg/m^3)             | 622.09                  | 622.123                | 694.073                | 665.283               |
| Entalpia Parowania (kcal/mol) | 7.961221403             | 8.005923318            | 9.750799259            | 8.581317562           |
| Dyfuzja translacyjna (cm²/µs) | 1.9079 × 10<sup>-5</sup>| 2.2299 × 10<sup>-5</sup>| 4.2609 × 10<sup>-5</sup>| 3.3454 × 10<sup>-5</sup> |

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

