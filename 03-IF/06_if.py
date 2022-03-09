# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz
# do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od
# największej do najmniejszej.

number1 = int(input("wpisz liczbe całkowitą: "))
number2 = int(input("wpisz liczbe całkowitą: "))
number3 = int(input("wpisz liczbe całkowitą: "))

if number1 > number2 and number1 > number3:
    print("Liczba nr 1 jest najwiekasza", number1)
elif number2 > number1 and number2 > number3:
    print("liczba nr 2 jest najwieksza", number2)
elif number3 > number1 and number3 > number2:
    print("liczba nr 3 jest największa", number3)





