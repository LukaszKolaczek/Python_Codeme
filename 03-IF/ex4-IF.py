# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. W
# yświetl różne komunikaty w zależności od rodzaju błędu.

password = input("podaj haslo: ")
if password == "Haslo123":
    print("Twoje hasło jest prawidłowe")

elif len(password) < 8:
    print("twoje haslo jest za krotkie")

elif password.islower():
    print("haslo powinno zawierac co najmniej 1 duza litere")

elif password.isupper():
    print("haslo powinno zawierac co najmniej 1 mala litere")

elif password.isalnum() or password.isdigit():
    print("haslo musi miec cyfry i litery")
else:
    print("Towje haslo jest nie prawidlowe")