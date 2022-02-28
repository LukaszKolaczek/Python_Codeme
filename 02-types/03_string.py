quote = "Honesty is the first chapter in the book of wisdom."
# Policz wszystkie znaki w napisie
print(len(quote))
# Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])
# Wyświetl tylko pierwszą połowę tekstu
print(quote[0:25])
# Wyświetl tylko kropkę
print(quote[-1:])
# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[25::3])
# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])
# Wyświetl cały cytat odwrotnie
# tu nic nie moge znaleść
# Zamień wisdom na słowo friendship
print(quote.rstrip("wisdom.") + "friendship")


