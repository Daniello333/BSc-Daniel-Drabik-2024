import matplotlib.pyplot as plt

def generate_plot():
    # Dane do wykresu
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Generowanie wykresu
    plt.plot(x, y)
    plt.xlabel('Wartość X')
    plt.ylabel('Wartość Y')
    plt.title('Wykres przykładowy')
    plt.grid(True)
    plt.savefig('plot.png')  # Zapisywanie wykresu do pliku plot.png
    plt.show()

if __name__ == "__main__":
    generate_plot()
