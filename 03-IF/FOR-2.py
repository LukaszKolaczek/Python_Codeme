# Utwórz listę, która zawiera składniki na ulubione danie.
# Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe
# instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

meal = ['makaron', 'sos spagetti', 'ser']

for skladniki in meal:
    print(skladniki)
    if skladniki == 'makaron':
        print("należy ugotować makaron")
    elif skladniki == 'sos spagetti':
        print("należy podgrzć sos spagetti")
    elif skladniki == "ser":
        print("należy zetrzć ser i posypać danie")