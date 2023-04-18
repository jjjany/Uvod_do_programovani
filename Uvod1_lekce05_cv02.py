# Jednoduchý vstup

# Teď už budeme chtít, aby náš program dokázal získat vstup od uživatele.

#     a) Napište program jmeno.py, který získá jméno a příjmení od uživatele voláním funkce input(). Vypište je na obrazovku podobně jako v předchozím cvičení.
jmeno = input("Napiš své křestné jméno:")
prijmeni = input("Napiš své příjmení:")
print(f"\n {jmeno} {prijmeni}\n")

#     b) Nechte uživatele zadat také věk. Pozor na to, že funkce input() vždy vrací řetězec, ale my chceme v proměnné vek mít číslo. Použijte tedy funkci int(), abyste převedli uživatelem zadaný řetězec na číslo. Opět vypište na obrazovku jméno, příjmení a věk tak jako v předchozí verzi.
vek = str(input("Napiš svůj věk:"))
print(f"\n Celé jméno: {jmeno} {prijmeni}, věk: {vek}\n")