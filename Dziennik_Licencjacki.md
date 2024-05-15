
# Praca licencjacka
## Wyznaczanie właśności kinetycznych związków aktywnych biologicznie z wykorzystaniem metody modelowania molekularnego
## Cele badawcze
* Cele pośrednie:
	* n-pentadekan dla OPLS/AA-2022 i C36 (2014, 2021) (trzeba będzie przepisać niektóre parametry)
	* density, heat of vaporization - sprawdzenie poprawności parametryzacji cząsteczek n-pdc
* Cel główny: 
	* własności kinetyczne - obliczenia dyfuzji translacyjnej, rotacyjnej i ew. lepkości
# Spotkania z promotorem w ramach pracowni
## 2024-15-05
* Zapisać lepiej pierwszy rząd w tabelce
* Wstawić te wartości z publikacji dla porównanie do tabeli
* Podanie wartości eksperymentalnej
* Podanie Wersji Gromacsa : 2022.4-conda_forge
* Podanie Wersji Gromacsa z publikacji
* Zmiana tytułu :Wyznaczanie własności termodynamicznych i kinetycznych n-oktanu, n-dodekanu i n-pentadekanu metodami modelowania molekularnego
* Obliczenia dla cząsteczek : oktan, dodekan, pentadekan (który już mam)

* Oryginalny OPLS : OPLS_1996
* JPCB OPLS : OPLS_2013
* Jorgensen JPCB : OPLS_2022
* CHARMM_C36

*Do katalogów VOID wstawić pliki top i itp
## 2024-08-05
* Stworzenie dokumentu zbiorczego w którym będą się znadjowały:
	* Podrozdziały dla odpowiednich pól siłowych
   	* Kilkuzdaniowy opis przebiegu obliczeń
   	* Zestawienie wszystkich parametrów dla podzespołów
   	* tabelki dla entalpii swobodnej hydratacji, dyfuzji translacyjnej i gęstości
* Główny cel : sprawdzenie poprawności topologii cząsteczek z publikacji
* Dodatkowo : obliczenie energii swobodnej hydratacji delta G
* Stworzenie podkatalogów VOID :
	* plik dla pojedynczej cząsteczki
   	* pierwsza i ostatnia klatka z fazy ciekłej w formacie pdb
* Wykresy matplotlib - formatowanie - tutorial
* Stworzyć pliki z wykresami z rozszerzeniem py
  
## 2024-24-04
* Stworzenie plików void.mdp dla pól siłowych OPLS i C36 dla pentadekanu.
* Obliczenie dwóch pól siłowych OPLS
* Obliczenie entalpii parowania
* Następny krok po entalpii parowania - weryfikacja poprawnie zbudowanej cząsteczki - porównanie z wynikami eksperymentalnymi
* Jeśli jest poprawnie - Policzenie gęstości - sprawdzenie poprawności cząsteczki
* Policzenie dyfuzji translacyjnej
* Porównanie pól siłowych
* Dane do umieszczenie w DATA: minimalny zestaw plików : plik top, mdp, itp
* Zwrócenie się do Pana Michała w sprawie obliczenia dyfuzji translacyjnej
* Symulacje w temperaturze (sprawdzić w publikacji w jakiej temperaturze)
* Minsquare displacement

## 2024-10-04
* Pudełko symulacyjne = 3,5 -4 max
* Policzenie gęstości -> Gmx energy dla Production_MD -> Wybranie Density
* Policzenie energii potencjalnej -> Gmx energy dla Production_MD -> Wybranie Potential
* Policzyć Hvap dla pentadekanu
* Stworzyć biblioteke z publickacjami : MacKerell Lab (umaryland.edu)  CHARMM 36
* Refinement of the Optimized Potentials for Liquid Simulations Force Field for Thermodynamics and Dynamics of Liquid Alkanes | The Journal of Physical Chemistry B (acs.org)
* OPLS/AA aktualizacja 2022 -> Uwzględnić pole siłowe. 
* nienasycone węglowodory, alkohole i estry - 2024 (Jorgensen Publications)
* trójacetyna i n-pentadekan
* Stwórz w data: 
	* Katalog n-pentadekan
	* Podkatalogi opls i c36
* Cele pośrednie:
	* n-pentadekan dla OPLS/AA-2022 i C36 (2014, 2021) (trzeba będzie przepisać niektóre parametry)
	* density, heat of vaporization - sprawdzenie poprawności parametryzacji cząsteczek n-pdc
* Cel główny: 
	* własności kinetyczne - obliczenia dyfuzji translacyjnej, rotacyjnej i ew. lepkości

  
## 2024-03-04

 * Nieudane obliczenia w GROMACS dotyczące pentadekanu: w trakcie przeprowadzania symulacji molekularnej pentadekanu w programie GROMACS napotkaliśmy na pewne problemy, które wymagały zastosowania dodatkowych kroków w celu poprawienia stabilności symulacji.

* opis problemu: podczas standardowej symulacji z użyciem zwykłego termostatu, zauważyliśmy, że temperatura systemu nie stabilizuje się prawidłowo, co może prowadzić do błędnych wyników. 

* rozwiązanie: Aby poprawić stabilność symulacji, zastosowaliśmy metodę Berendsena, która umożliwia lepszą kontrolę temperatury w systemie. Metoda ta dodaje dodatkową siłę do równań ruchu, co pozwala na lepszą regulację temperatury, zwłaszcza w przypadku substancji, które mają trudności w osiągnięciu równowagi termicznej.
Dodatkowo, aby przyspieszyć proces równowagi i zbliżyć system do warunków docelowych, zdecydowaliśmy się zwiększyć temperaturę do 50 stopni Celsjusza. 

## 2024-10-03
* Połączenie Visual Studio Code z Repozytorium GitHuba za pomocą środowiska Codespace 
    * Komendy : clone, commit, push 
* Wykonane obliczenia dla trójacetyny 
* Dane i wyniki symulacji 
    * Energia potencjalna dla pojedynczej cząsteczki : -158,486 kJ/mol 
    * Energia potencjalna dla 800 cząsteczek trójacetyny : -182196 kJ/mol
    * Ilość cząsteczek (N) : 800
    * Temperatura : 298,15 K
    * Wyliczona entalpia parowania : 71,73782 kJ/mol = 17,14534 kcal/mol
    


