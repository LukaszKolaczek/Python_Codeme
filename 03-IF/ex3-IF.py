# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

book1 = int(input("Twoja opinia w skali od 1 -10: "))
book2 = int(input("Twoja opinia w skali od 1 -10: "))
book3 = int(input("Twoja opinia w skali od 1 -10: "))

if (book1 + book2 + book3) / 3 >= 7:
    print("bardzo dobra")
elif (book1 + book2 + book3) / 3 < 7 > 5: #-->> do potprawy
    print("przecietna")
elif (book1 + book2 + book3) / 3 <= 4:
    print("nie warta uwagi")