# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

suma = 1
for number in range(10):
    suma = suma + number
    print(suma + number)
