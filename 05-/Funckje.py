#napisz funkcje ktora pyta o ksiazke i ocene

books = {}

def ask_for_book():
    book_title = input("podaj tytul książki: ")
    book_rate = input('podaj ocene ksiazki 1-10: ')
    books[book_title] =  book_rate

for i in range(3):
    ask_for_book()
    print('_____')

print(books)