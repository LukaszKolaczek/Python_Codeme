# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę
# ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

win = 24
liczba = int(input("wpisz liczbe od 1-100: "))

if liczba == win:
    print("gratulacje")
else:
    print("pudło")
