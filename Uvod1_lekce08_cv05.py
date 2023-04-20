# Průměr

# Napište cyklus, který projde zadaný seznam desetinných čísel a spočítá jejich průměr. Seznam čísel si vytvořte na začátku programu.
cisla = [
    0.4522,
    1.133,
    7.25,
    3.012,
    0.796,
    7.7496,
    6.43
]

suma = 0
for cislo in cisla:
    suma = suma + cislo
prumer = suma/len(cisla)
print(prumer)

# bez cyklu
print(sum(cisla)/len(cisla))
