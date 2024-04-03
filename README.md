
# Spotkania z promotorem w ramach pracowni

## 2024-04-03

 * Nieudane obliczenia w GROMACS dotyczące pentadekanu: w trakcie przeprowadzania symulacji molekularnej pentadekanu w programie GROMACS napotkaliśmy na pewne problemy, które wymagały zastosowania dodatkowych kroków w celu poprawienia stabilności symulacji.

* opis problemu: podczas standardowej symulacji z użyciem zwykłego termostatu, zauważyliśmy, że temperatura systemu nie stabilizuje się prawidłowo, co może prowadzić do błędnych wyników. 

* rozwiązanie: Aby poprawić stabilność symulacji, zastosowaliśmy metodę Berendsena, która umożliwia lepszą kontrolę temperatury w systemie. Metoda ta dodaje dodatkową siłę do równań ruchu, co pozwala na lepszą regulację temperatury, zwłaszcza w przypadku substancji, które mają trudności w osiągnięciu równowagi termicznej.
Dodatkowo, aby przyspieszyć proces równowagi i zbliżyć system do warunków docelowych, zdecydowaliśmy się zwiększyć temperaturę do 50 stopni Celsjusza. 


