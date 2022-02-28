# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
book = input("Podaj tytuł książki:")
author = input("Podaj nazwisko autora:")
page = int(input("Jaka jest liczba storn:"))
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

# Połącz dane w jeden ciąg book za pomocą spacji
print(book + " " + author + " " + str(page))
# Policz liczbę wszystkich znaków w napisie book
print(len(Book)) #-->> nie dziala
