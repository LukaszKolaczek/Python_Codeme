# Stwórz zmienną przechowującą
# wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.


txt = "LukaszKolaczek-" #---> 15 znaków
mid_txt = len(txt) //2 #---> 7 znaków
first_mid_txt = mid_txt -1 #---> 6 znak
secound_mid_txt = mid_txt +1  #---->8 znak

print(txt[first_mid_txt:secound_mid_txt +1]) # txt[6:9]to potrzbujemy
