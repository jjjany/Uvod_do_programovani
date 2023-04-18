# Zakázka pro divadlo

# Divadlo požaduje systém pro online rezervaci vstupenek na pořádaná představení. Váš první úkol na této zakázce je vytvořit registraci pro nové uživatele tohoto systému.

#     a) Založte si program vstupenky01.py. Bude to první verze našeho programu pro nákup vstupenek.

#     b) Napište program tak, aby nejprve vypsal na obrazovku Divadlo Pěst na oko na první řádek, na druhý řádek chceme vypsat Vítejte v online rezervaci vstupenek a na třetí řádek Pro vstup do systému je potřeba registrace.
print(f"\nDivadlo Pěst na oko \nVítejte v online rezervaci vstupenek\nPro vstup do systému je potřeba registrace\n")

#     c) Na dalším řádku požádejte uživatele o jeho uživatelské jméno a poté o jeho věk. Ten si uložte do nějaké proměnné jako číslo.
uziv_jm = input("Zadejte své uživatelské jméno (bez diakritiky):")
vek = int(input("Zadejte svůj věk (cele cislo):"))
print("\n")