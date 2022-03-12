import random
hit = random.randint(1,2)
run = random.randint(1,2)
trap = random.randint(1,2)
boss = random.randint(1,5)

print("Obudziłęś się w dziwnym pomieszczeniu,")
print("Widzisz drzwi a na nich kartkę z namisem 'mamy twoją dziewczyne, przynieś 1m$'  ")

exit_game = input("czy chcesz wyść [Y/N]: ")
if exit_game == "Y":
    print("Drzwi się otwirają i widzisz labirynt")
else:
   breakpoint(print("Do pomieszczenia wrzucają martwe ciało towjej dzierczyny"))

trip1 = input("widzisz na korytarze w lewo[1] i w prawo[2], który wybierasz: ")
if trip1 == "1":
    print("Idziesz w lewo i po paru minutach napotykasz dziwnie odzianego przeciwnika, a zanim kolejne drzwi")
    trip1_1 = (input("walczysz czy uciekasz[W/U]: "))
    if trip1_1 == "W":
        print("zaczynasz walkę i uderzasz")
        print("==============")
        if hit == 2:
            print("pokonujesz przeciwnika mozesz iść dalej")
            print("idziesz dalej i napotykasz napotykasz psa")
            print(input("czy chcesz go pogłaskać? [Y/N]: "))
            print("nic sie nie wydażyło")

            happy_end = input("Po podruży która trwałą całę 1min i 34s, napotykasz związaną dziwczyne i wpułapce, ktora ja zabije czy chcesz ją rozwiązać?[Y/N]: ")
            if happy_end == "Y":
                if trap == 1:
                    print("ratujesz ją")
                    joke = input("Rozwiązujesz swoją wybrankę, czy chcesz zobaczyć i rozmowę po uwatorniu? [Y/N]: ")
                    if joke == "Y":
                        print("Dziewczyna: Dziekuję ukochany teraz, zasługujesz na pocałunek")
                        print(
                            "Bohater: Pocałunek?!?!? Ja ratuję Cię pokonując labirynt i przeciwników, którzy mogli mnie zabić")
                        print("i chcesz dac tylko buziaka, ŚCIĄGAJ SPODNIE!!!")
                        breakpoint(print("KONIEC"))
                    else:
                        breakpoint(print("Uciekacie i żyjecie długo i szcześliwie"))
                else:
                    breakpoint(print("ginie ale może uda Ci się ułożyć życie lepiej kto to wie"))



        else:
           breakpoint(print("zostałeś pokonany"))

    elif trip1_1 == "U":
            breakpoint(print("przeciwnik cie złapał i zabił"))

elif trip1 == "2":
    print("idziesz korytarzem i widzisz kolejne drzwi")
    print("otwirasz je i widzisz przeciwnika tak dużgo jakiego jeszcze nie widziałeś")
    boss_fight = input("czy chcesz walczyc z takim gościem [Y/N]:")
    if boss_fight == "Y":
        if boss > 1:
            print("Ostakiem sił pokonałęś tego wielkiego przeciwnika, w telewizorze na ścianie widzisz swoją wybranke")
            print("która została zabita przez pułapkę.")
            breakpoint(print("widzisz drzwi przez które uciekasz i możesz życ dalej może równie szcześliwie"))
        else:
            breakpoint(print("przeciwnik był za mocny i cie zabija :("))

else:
    breakpoint(print("Słyszysz kroki i widzisz przeciwnika, który Cię zabija"))