from PyQt5.QtWidgets import QFileDialog, QApplication
import sys
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

from funkcje import Funkcje
from interpolacja import Interpolacja

def main():
    while True:
        wybor_opcji = input("""
__________________________________________________________
T: load a function from a file
G: pick a defined function
Q: exit
__________________________________________________________
""").lower()
        if wybor_opcji == 'q':
            print("Exit")
            break
        elif wybor_opcji == 'g':
            wybor_funkcji = input("""
______________________________________________________
                Pick a function:
______________________________________________________
A: 4*x^3 + 2*x^2 - 8*x + 4
B: 8 * cos(x) - 2 * sin(x)
C: exp(x) + 9
D: x + 18
E: |cos(x - 1) - 0.8|
______________________________________________________
Choice: """).upper()
            lewy_przedzial = int(input("Enter a beginning of a sector: "))
            prawy_przedzial = int(input("Enter an end of a sector: "))
            liczba_wezlow_interpolacyjnych = int(input("Enter how many nodes: "))
            argumenty = np.linspace(lewy_przedzial, prawy_przedzial, 1000)
            wartosci_funkcji = [Funkcje.wartosc_funkcji(arg, wybor_funkcji) for arg in argumenty]
            plt.plot(argumenty, wartosci_funkcji, label='graph f(x)')
            plt.title('f(x)=' + str(Funkcje.wzor_funkcji(wybor_funkcji)))
            x_pkt_inter = np.linspace(lewy_przedzial, prawy_przedzial, liczba_wezlow_interpolacyjnych)
            y_pkt_inter = Funkcje.wartosc_funkcji(x_pkt_inter, wybor_funkcji)
            plt.scatter(x_pkt_inter, y_pkt_inter, label='interpolar nodes')
            wzor_interpolacji_wprzod = Interpolacja.interpolacja_wprzod(x_pkt_inter, y_pkt_inter)
            wzor_interpolacji_wstecz = Interpolacja.interpolacja_wstecz(x_pkt_inter, y_pkt_inter)
            plt.plot(argumenty, [wzor_interpolacji_wprzod.subs('x', arg) if arg < (lewy_przedzial + prawy_przedzial) / 2 else wzor_interpolacji_wstecz.subs('x', arg) for arg in argumenty], linestyle=":", label='interpolar polynomial')
            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid(True)
            plt.legend(loc='upper right')
            plt.show()
        elif wybor_opcji == 't':
            app = QApplication(sys.argv)

            file_path, _ = QFileDialog.getOpenFileName(None, "Wybierz plik txt", "", "Pliki tekstowe (*.txt)")

            if file_path:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    pass
            else:
                print("Nie wybrano pliku.")


            x_pkt_inter = list(map(float, lines[0].split(',')))
            y_pkt_inter = list(map(float, lines[1].split(',')))

            lewy_przedzial = min(x_pkt_inter)
            prawy_przedzial = max(x_pkt_inter)

            argumenty = np.linspace(lewy_przedzial, prawy_przedzial, 1000)

            plt.scatter(x_pkt_inter, y_pkt_inter, label='interpolar nodes')

            wzor_interpolacji_wprzod = Interpolacja.interpolacja_wprzod(x_pkt_inter, y_pkt_inter)
            wzor_interpolacji_wstecz = Interpolacja.interpolacja_wstecz(x_pkt_inter, y_pkt_inter)

            plt.plot(argumenty, [wzor_interpolacji_wprzod.subs('x', arg) if arg < (lewy_przedzial + prawy_przedzial) / 2 else wzor_interpolacji_wstecz.subs('x', arg) for arg in argumenty], linestyle=":", label='interpolar polynomial')

            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid(True)
            plt.legend(loc='upper right')
            plt.show()
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()
