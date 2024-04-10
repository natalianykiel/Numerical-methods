import easygui
import numpy as np
from jordan import Jordan

n = 0

print("""Welcome to the software that solves the system of N linear equations with the N unknown Jordan elimination method. Select data entry options:
                F - from text file
                M - manually
            """)
mode = input("Press F or M to continue ").upper()

if(mode == 'M'):
    print('Enter number of unknowns: ')
    while n >= 10 or n <= 0:
        n = int(input())
    a = np.zeros((n,n+1))
    x = np.zeros(n)

    print('Enter Augmented Matrix Coefficients:')
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

    jo = Jordan()
    jo.matrix = a
    jo.vector = x
    jo.n = n
    jo.jordan()
elif(mode == "F"):
    file_path = easygui.fileopenbox()

    # otwórz plik
    with open(file_path, 'r') as f:
        lines = f.readlines()

    matrix = []
    vector = []

    # dla każdego wiersza w pliku
    for line in lines:
        # podziel linie na liczby
        numbers = list(map(float, line.split(',')))

        # dodaj wszystkie liczby poza ostatnią do macierzy
        matrix.append(numbers[:-1])

        # dodaj ostatnią liczbę do wektora
        vector.append(numbers[-1])

        n = n+1

    print("Matrix:", matrix)
    print("Vector:", vector)

    jo = Jordan()
    jo.matrix = matrix
    jo.vector = vector
    jo.jordan()

input("\nPress Enter to continue...")