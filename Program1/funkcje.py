import numpy as np

from horner import Horner

class Funkcje:
    #zwraca jej wartosc funkcji 
    def f(x, wybor):
        if wybor == "A":    #WIELOMIAN
            y = Horner.horner([7, 3, 2, -7], x)  
        elif wybor == "B":  #TRYGONOMETRYCZNA 
            y = 2 * np.cos(x) - 2 * np.sin(x)
        elif wybor == "C":  #WYKŁADNICZA
            y = 2**x-5**x + 4
        elif wybor == "D":  #ZŁOŻONA
            y = 2 *np.sin(x)+2*x**2-1 + 7 * x
        else:
            print("Podano nieprawidlowa wartosc.")
            y = None
        return y

    #zwraca wartosc pochodna funkcji
    def df(x, wybor):
        if wybor == "A":    #WIELOMIAN
            df = Horner.horner([3, 4, -21], x)
            #y = (-21) * x * x   + 4 * x + 3
        elif wybor == "B":  #TRYGONOMETRYCZNA 
            df = (-2) * np.cos(x) - 2 * np.sin(x)
        elif wybor == "C":  #WYKŁADNICZA
            df = (2**x) * np.log(2) - (5**x) * np.log(5)
        elif wybor == "D":  #ZŁOŻONA
            df = 4 * x + 2 * np.cos(x) + 7
        else:
            print("Podano nieprawidlowa wartosc.")
            df = None
        return df