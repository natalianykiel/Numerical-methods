import matplotlib.pyplot as plt
import numpy as np
from funkcje import Funkcje

class Bisekcja:
    def metoda_bisekcji (self):
            a = self.a 
            b= self.b 
            #eps = self.eps
            iteracje = self.iteracje
            wybor = self.wybor
            i = iteracje
            if (Funkcje.f(a, wybor) * Funkcje.f(b, wybor) > 0):
                    return False 
            else:
                if iteracje <= 0:  #KRYTERIUM DOKŁADNOSCI
                    n=0
                    while True:
                        self.iteracje = n
                        c = (a + b) / 2.0
                        dfc = Funkcje.df(c, wybor)
                        if abs(Funkcje.f(c, wybor)) <= self.eps and (abs(Funkcje.df(c, wybor)) > self.eps):
                            self.eps = abs(Funkcje.f(c, wybor))
                            print('x = {:.6f}'.format(c))
                            return c
                        elif Funkcje.f(c, wybor) * Funkcje.f(a, wybor) < 0:
                            b = c
                        else:
                            a = c
                        n += 1
                else:  #KRYTERIUM ITERACYJNE
                    for i in range(iteracje):
                        c = (a + b) / 2.0
                        if Funkcje.f(c, wybor) == 0:
                            print('x = {:.6f}'.format(c))
                            return c
                        if Funkcje.f(c, wybor) * Funkcje.f(a, wybor) < 0:
                            b = c
                        else:
                            a = c
                    print('x = {:.6f}'.format(c))
                    return c
    
    def plot_function_and_zero(self):
        x = np.linspace(self.a - 1, self.b + 1, 1000)  # Zakres x dla wykresu
        y = Funkcje.f(x, self.wybor)

        plt.plot(x, y, label="Funkcja {}".format(self.wybor))
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')

        zero = self.metoda_bisekcji()  # Znajdowanie miejsca zerowego

        if zero != False:
            plt.scatter(zero, 0, color='green', marker='x', label='Miejsce zerowe z metody bisekcji')


        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.title('Wykres funkcji')
        plt.grid(True)
        
        # Zaznaczanie wybranego zakresu
        plt.axvline(self.a, color='green', linestyle=':', label='Początek przedziału')
        plt.axvline(self.b, color='blue', linestyle=':', label='Koniec przedziału')

        plt.xlim([self.a - 1, self.b + 1])

        plt.show()
    