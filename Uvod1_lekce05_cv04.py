# Házení kostkami

# Napište program kostky.py, který bude simulovat hod dvěma klasickými šestistěnnými kostkami. Jeho výstupu bude součet bodů na těchto dvou kostkách.

# Nápověda:

#     Generování náhodných čísel dělá funkce random.randint().
#     Pokud chcete ve vašem programu použít modul random, musíte na jeho úplném začátku napsat příkaz "import random"

from random import randint
kostka_1 = randint(1,6)
kostka_2 = randint(1,6)
soucet = kostka_1 + kostka_2

print(f"\nHázím dvěmi kostkami.\nNa první kostce padlo číslo {kostka_1}.\nNa druhé kostce padlo číslo {kostka_2}.\nSoučet je {soucet}\n")