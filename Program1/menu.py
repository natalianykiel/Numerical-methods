from styczne import Styczne
from bisekcja import Bisekcja


def menu():
    print("""Witaj w programie obliczajacym rozwiazania rownan liniowych metoda bisekcji lub stycznych:
            A- funkcja wielomianowa: -7x^3+2x^2+3x+7
            B- funkcja trygonometryczna: 2*cos(x)-2*sin(x)
            C- funkcja wykladnicza: 2^x-5^x+4
            D- funkcja zlozona: 2*sin(x)+2*x^2-1+7x
            """)
    return input("Wpisz A, B, C lub D, wybierz Q zeby zakonczyc: ").upper()

def wybor_metody():
    return input("""Wybierz metode rozwiązywania równań algorytmu:
                b- metoda bisekcji
                s- metoda stycznych\n""").lower()

def przedzial(P):
    try:
        value = int(input("Podaj " + str(P) +  " przedzial: "))   # wybor przedzialu funkcji
    except ValueError:
        print("Podaj prawidlowa calkowita liczbowa wartosc poczatku przedzialu")
        value = przedzial(P)
    return value

def kryterium():
    return input("""Wybierz kryterium zatrzymania algorytmu:
                d- spelnienie warunku nalozonego na dokladnosc
                i- osiagniecie zadanej liczby iteracji\n""").lower()

def inputEps():
    try:
        eps = abs(float(input("Podaj dokladnosc epsilon: ")))
    except ValueError:
        print("Podaj prawidlowa liczbowa wartosc dokladnosci epsilon")
        eps = inputEps()
    return eps

def inputIteracji():
    try:
        liczba_iteracji = int(input("Podaj liczbe iteracji: "))
        if liczba_iteracji < 0:
            print("Podaj prawidlowa calkowita dodatnia wartosc liczby iteracji")
            liczba_iteracji = inputIteracji()
    except ValueError:
        print("Podaj prawidlowa calkowita dodatnia wartosc liczby iteracji")
        liczba_iteracji = inputIteracji
    
    return liczba_iteracji


metoda = " "
wybor_funkcji = " "
wybor_kryterium = " "
lewy_przedzial = 0
prawy_przedzial = 0
eps = 0
liczba_iteracji = 0

while wybor_funkcji not in "ABCDQ":
    wybor_funkcji = menu()

if wybor_funkcji == "Q":
    print("Koniec Programu")
else:
    while metoda not in "bs":
        metoda = wybor_metody()

    while lewy_przedzial >= prawy_przedzial:
        lewy_przedzial = przedzial("lewy")
        prawy_przedzial = przedzial("prawy")
        if lewy_przedzial >= prawy_przedzial:
            print("Nieprawidłowy przedział. Wprowadź ponownie.")

    while wybor_kryterium not in "di":
        wybor_kryterium = kryterium()

    if wybor_kryterium == 'd':
        liczba_iteracji = 0
        while eps <= 0.0:
            eps = inputEps()
    elif wybor_kryterium == 'i':
        eps = 0.0
        while liczba_iteracji <= 0:
            liczba_iteracji = inputIteracji()

    if metoda == 'b':
        print("""Metoda Bisekcji:
              Wybrana funkcja: """ + wybor_funkcji + """
              Przedział: (""" + str(lewy_przedzial) + ", " + str(prawy_przedzial) + """)
              Eps: """+ str(eps) + """
              Iteracje: """ + str(liczba_iteracji))
        
        bi = Bisekcja()
        bi.a = lewy_przedzial
        bi.b = prawy_przedzial
        bi.eps = eps
        bi.iteracje = liczba_iteracji
        bi.wybor = wybor_funkcji
        bi.plot_function_and_zero()
        print("Eps: "+ str(bi.eps) + " Iteracje: " + str(bi.iteracje))

    elif metoda == 's':
        print("""Metoda Stycznych:
              Wybrana funkcja: """ + wybor_funkcji + """
              Przedział: (""" + str(lewy_przedzial) + ", " + str(prawy_przedzial) + """)
              Eps: """+ str(eps) + """
              Iteracje: """ + str(liczba_iteracji))
        sty = Styczne()
        sty.a = lewy_przedzial
        sty.b = prawy_przedzial
        sty.eps = eps
        sty.iteracje = liczba_iteracji
        sty.wybor = wybor_funkcji
        sty.plot_function_and_zero()
        print("Eps: "+ str(sty.eps) + " Iteracje: " + str(sty.iteracje))

    



