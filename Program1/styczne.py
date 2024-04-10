from funkcje import Funkcje
import matplotlib.pyplot as plt
import numpy as np

class Styczne:
    def metoda_stycznych(self):
            a = self.a 
            b= self.b 
            #eps = self.eps
            iteracje = self.iteracje
            wybor = self.wybor
        #WARUNKI POCZĄTKOWE
            if Funkcje.f(a, wybor) * Funkcje.f(b, wybor) > 0:
                return False
            if abs(Funkcje.df(a, wybor)) < abs(Funkcje.df(b, wybor)):
                c = b
            elif abs(Funkcje.df(a, wybor)) > abs(Funkcje.df(b, wybor)):
                c = a
            else:
                c = (a + b) / 2.0
            i = iteracje
            #WARUNKE ITERACJI
            if iteracje > 0:
                while iteracje > 0:
                    fc = Funkcje.f(c, wybor)
                    dfc = Funkcje.df(c, wybor)
                    c = c - float(fc/dfc)
                    iteracje -= 1
                self.eps = abs(Funkcje.f(c, wybor))
                print('x = {:.6f}'.format(c))
                return c
            else: #WARUNEK DOKŁADNOŚCI
                n=1
                while True:
                    self.iteracje = n
                    fc = Funkcje.f(c, wybor)
                    dfc = Funkcje.df(c, wybor)
                    if(abs(fc) < self.eps) and (abs(dfc) > self.eps):
                        print('x = {:.6f}'.format(c))
                        #print('Metoda stycznych:znaleziono rozwiazanie po ', n + 1, 'iteracjach.')
                        return c
                    c = c - ((float)(fc / dfc))
                    n += 1
    def plot_function_and_zero(self):
        x = np.linspace(self.a - 1, self.b + 1, 1000)  # Zakres x dla wykresu
        y = Funkcje.f(x, self.wybor)

        plt.plot(x, y, label="Funkcja {}".format(self.wybor))
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')

        zero = self.metoda_stycznych()  # Znajdowanie miejsca zerowego

        if zero != False:
            plt.scatter(zero, 0, color='red', marker='o', label='Miejsce zerowe z metody stycznych')

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