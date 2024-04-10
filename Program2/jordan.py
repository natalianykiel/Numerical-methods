import numpy as np

class Jordan:
    def swap_rows(self, matrix, vector, k, n):
        # Wyszukiwanie maksymalnej wartości bezwzględnej w kolumnie
        max_val = abs(matrix[k][k])
        index = k
        for i in range(n - k):
            if abs(matrix[k + i][k]) > max_val:
                max_val = abs(matrix[k + i][k])
                index = k + i
        
        # Zamiana wierszy, jeśli maksymalna wartość nie jest na przekątnej
        if index != k:
            buffer_list = [0] * n
            for i in range(n):
                buffer_list[i] = matrix[k][i]
                matrix[k][i] = matrix[index][i]
                matrix[index][i] = buffer_list[i]
            buffer_val = vector[index]
            vector[index] = vector[k]
            vector[k] = buffer_val
        
        return matrix, vector

    def jordan(self):
        # Tworzenie kopii macierzy i wektora
        matrix = self.matrix[:]
        vector = self.vector[:]
        n = len(vector)
        
        for k in range(n):
            # Sprawdzenie, czy wiersz zawiera same zera
            all_zeros = all(round(value, 8) == 0 for value in matrix[k])
            if all_zeros:
                # Sprawdzenie, czy równanie jest sprzeczne lub nieoznaczone
                if round(vector[matrix.index(matrix[k])], 8) == 0:
                    print("Układ nieoznaczony")
                else:
                    print("Układ sprzeczny")
                return None
            
            # Wywołanie metody swap_rows w celu ewentualnej zamiany wierszy
            matrix, vector = self.swap_rows(matrix, vector, k, n)
            
            # Dzielenie wiersza głównego przez jego element diagonalny
            pivot = matrix[k][k]
            vector[k] /= pivot
            for j in range(n - k):
                matrix[k][k + j] /= pivot
            
            for i in range(n):
                if i != k:
                    factor = matrix[i][k]
                    vector[i] -= vector[k] * factor
                    for j in range(n):
                        matrix[i][j] -= matrix[k][j] * factor
        
        # Zaokrąglenie wyników
        vector = [round(x, 8) for x in vector]
        
        # Wydruk rozwiązania
        print('\nRequired solution is: ')
        for i in range(n):
            print('X%d = %0.2f' %(i, vector[i]), end = '\t')
        return vector
