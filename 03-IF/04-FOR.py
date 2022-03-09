# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

n = int(input("wpisz liczę od 1 do 8: "))
silnia = 1

for i in range(n, 0, -1):
    silnia = silnia * n
    if n <=8:
        print('liczba jest oki')
    else:
        print("liczba jest za duza")

print("silnia z cyfry", n,"to", silnia)



