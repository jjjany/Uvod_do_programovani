# Generátor čísel

# Napište program generator.py, který si od uživatele vyžádá dvě celá čísla - dolní mez a horní mez - a vypíše na výstup náhodné číslo v zadaných mezích.
from random import randint

print(f"\nJsem generátor náhodných čísel. Zadáš-li mi dvě hodnoty (dolní a horní mez), vygeneruji ti náhodné číslo v daném intervalu.\n")
a = int(input("Zadej menší celé číslo:"))
b = int(input("Zadej větší celé číslo:"))
print(f"Náhodně vygenerované v zadaném rozsahu je {randint(a,b)}.\n")
