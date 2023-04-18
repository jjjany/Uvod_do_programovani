# Dělitelnost více čísly

# Požádejme uživatele, ať zadá celé číslo. Napiš program který zjistí, zda je číslo dělitelné 3 i 4 současně.

# Tip: nezapomeňte si zadané číslo převést na int. 
# Tip 2: K ověření dělitelnosti použij operátor % - zbytek po celočíselném dělení a zkontroluj, zda je výsledek 0. Například 15 % 5 vrací 0, protože 15 je dělitelné 5.
numb_a = 3
numb_b = 4
print(f"\nDělitelnost {numb_a} a {numb_b}.\n")
numb = int(input("Zadej celé číslo: "))

if (numb % numb_a == 0) and (numb % numb_b == 0):
    print(f"Číslo {numb} je dělitelné {numb_a} a zároveň {numb_b}.\n")
else:
    print(f"Číslo {numb} není zároveň dělitelné oběma čísly {numb_a} a {numb_b}.\n")
