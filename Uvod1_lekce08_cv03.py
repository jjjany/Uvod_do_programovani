# Složitější seznam

# Založte si program cykly02.py a použijte v něm následující seznam měsíců v roce, Všimněte si, že je to seznam seznamů.

mesice = [
    ["leden", 31],
    ["únor", 28],
    ["březen", 31],
    ["duben", 30],
    ["květen", 31],
    ["červen", 30],
    ["červenec", 31],
    ["srpen", 31],
    ["září", 30],
    ["říjen", 31],
    ["listopad", 30],
    ["prosinec", 31],
]

#     a) Pomocí cyklu projděte tento seznam a vypište na výstup názvy jednotlivých měsíců.
for mesic in mesice:
    print(mesic[0])

#     b) Pomocí dalšího cyklu vypište na výstup počty dní v jednotlivých měsících.
for mesic in mesice:
    print(mesic[1])
