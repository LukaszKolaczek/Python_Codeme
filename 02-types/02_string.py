#Stwórz dwie zmienne s1 i s2 przechowujące
# dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "lukas" #---> 5 znaków
s2 = "kolaczek"
miejsce = len(s1) // 2
s3 = (s1.rstrip("kas")) + s1[miejsce] + s2 + s1.lstrip("lu")

print(s3)

