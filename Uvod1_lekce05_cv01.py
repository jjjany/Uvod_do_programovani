# Jednoduchý výstup

# Náš vůbec první program nebude dělat nic víc, než vypisovat text na obrazovku.

#   a) Založte si program vstup-vystup.py. V tomto programu pomocí funkce print() vypište na obrazovku Divadlo Pěst na oko. Program spusťte a vyzkoušejte, že dělá co má.
print("\n", "Divadlo Pěst na oko", "\n")

#   b) Upravte tento program tak, že do proměnné nazev uložíte název nějakého divadelního představení a do proměnné cas uložte čas konání tohoto představení. Nyní pomocí funkce print() nechte program vypsat na obrazovku na jeden řádek název představení a čas konání, např. Zkrocení zlé ženy - 19:30.
nazev = "Potkali se u Kolína"
cas = "15:30"
print("\n", nazev, " - ", cas, "\n")

#   c) Upravte dále program tak, že do proměnné hodina uložíte hodinu konání představení (jako celé číslo) a do proměnné minuta minutu konání, také jako celé číslo. Zařiďte, aby výstup programu vypadal takto: Zkrocení zlé ženy - 19:30. Pozor na to, že hodina a minuta je hodnota typu číslo, takže ji budete při výpisu muset převést na řetězec pomocí funkce str().
hodina = 15
minuta = 30
print("\n", nazev, " - ", str(hodina) + ":" + str(minuta), "\n")
print(f"\n{nazev} - {str(hodina)}:{str(minuta)}\n")