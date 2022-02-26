#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

distance = int(input("wpisz dystans jaki chcesz pokonac [km]"))
cost = float(input("wpisz koszt paliwa za 1l [zl]:"))
usage = float(input("wpisz spalanie na 100km:"))

result = round(distance * cost * (usage / 100) , 2)

print(f'Koszt wyprawy bedzie wynosi: { result } zł')