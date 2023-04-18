# Cena vstupenky

# A nyní opět pokračujeme v našem rezervačním systému.

#     a) Program vstupenky01.py, který jste napsali v předchozí fázi, si uložte jako vstupenky02.py, abychom ho mohli dále rozšířit o výpočet ceny vstupenky.
print(f"\nDivadlo Pěst na oko \nVítejte v online rezervaci vstupenek\nPro vstup do systému je potřeba registrace\n")
uziv_jm = input("Zadejte své uživatelské jméno (bez diakritiky):")
vek = int(input("Zadejte svůj věk (cele cislo):"))
print("\n")

#     b) Jakmile máte v programu načtený věk uživatele, vytvořte si proměnnou plna_cena, do které uložte hodnotu 12.
plna_cena = 12

#     c) Vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel

#     0 euro pro návštěvníky mladší 6 let,
#     65% ze základní ceny pro návštěvníky 6 až 26 let (žák, student),
#     100% ze základní ceny pro návštěvníky 27 až 64 let (dospělý),
#     50% ze základní ceny pro ostatní (senior).

# Nezapomeňte na zaokrouhlování, ať nám cena vyjde v celých centech.
if vek < 6:
    cena = 0.0
elif vek <= 26:
    cena = round((plna_cena * 0.65), 2)
elif vek <= 64:
    cena = round((plna_cena * 1.00), 2)
else:
    cena = round((plna_cena * 0.50), 2)

#     d) Nakonec spočtenou cenu vypište s nějakou hezkou zprávou na výstup.
print(f"Děkujeme za vaši registraci. Každé představení vás u nás bude stát {cena}€.\nTěšíme se na vaši návštěvu.\n")
