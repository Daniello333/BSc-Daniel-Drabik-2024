
# Spotkania z promotorem w ramach pracowni

## 2024-04-03

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
    


