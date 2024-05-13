import matplotlib.pyplot as plt
import numpy as np

# Wczytanie danych z pliku, ignorując linie z komentarzami
data = np.loadtxt('energy_opls_2013_original.xvg', comments=['#', '@'])

# Podział danych na kolumny x i y
x = data[:, 0]  # Pierwsza kolumna
y = data[:, 1]  # Druga kolumna

# Tworzenie wykresu
plt.plot(x, y)

# Dodanie etykiet i tytułu
plt.xlabel('n_steps')
plt.ylabel('kJ/mol')
plt.title('OPLS_OLD_original_Energy')

# Wyświetlenie wykresu
plt.show()
