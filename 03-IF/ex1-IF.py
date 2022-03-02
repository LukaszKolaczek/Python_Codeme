# Poproś użytkownika o podanie liczby. Sprawdź czy
# liczba podana przez użytkownika jest podzielna
# przez 3 bez reszty i wyświetl komunikat “Twoja
# liczba jest podzielna przez 3”.

number = int(input("podaj liczbe: "))
if number % 3 == 0:
 print("twoja liczba jest podzielna przez 3")
else:
 print("twoja liczba nie jest podzielna przez 3")
