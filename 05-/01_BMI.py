def bmi(waga, wzrost):
   wynik = round(waga / wzrost ** 2, 2)
   if wynik < 18:
       return "niedowaga"
   elif wynik <25:
       return "waga w normie"
   elif wynik < 38:
       return "nadwaga"
   else:
       return "otyłość"


wynik = bmi(56, 1.6)
print(wynik)