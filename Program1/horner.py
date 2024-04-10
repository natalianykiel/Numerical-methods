class Horner:
    #wsp - liczba współczynników
    #stopień - njawieksza potęga wielomianu
    def horner(wsp, x):
        stopien = len(wsp) - 1
        wynik = wsp[stopien]    

        while stopien > 0:
            stopien = stopien - 1
            wynik = wynik * x + wsp[stopien]

        return wynik