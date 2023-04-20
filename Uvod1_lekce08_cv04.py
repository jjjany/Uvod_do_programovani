# Hry

# Následující seznam obsahuje seznam všech divadelních her, které se hrají v divadle Pěst na oko. Každá hra má svůj název a trvání v minutách.

hry = [
    ["Ňadro na ňadru na nádru", 180],
    ["Útok plyšových krokodýlů", 95],
    ["Cesta do říše zelí", 128],
    ["Romance na zdymadle", 144],
    ["Zátiší s mimozemšťanem", 135],
    ["Čtyři facky a dortík", 100],
    ["Motorová okurka", 165],
    ["Johnny Noir", 140],
    ["Pražská kavárna vrací úder", 130],
    ["Pět sester ve vratech", 111],
    ["Stařec a krajta", 187],
    ["Růžová nemoc", 210],
    ["Smrt v přímém přenosu", 265],
]

#     a) Pomocí cyklu projděte tento seznam a vypište na výstup názvy všech her.
for hra in hry:
    print(hra[0])

#     b) Vypište na výstup názvy všech her, které trvají více než 120 minut.
print("\n")
for hra in hry:
    if hra[1] > 120:
        print(hra[0])
    else:
        pass


#     c) Vypište na výstup názvy všech her spolu s jejich trváním v hodinách a minutách.
print("\n")
for hra in hry:
    hod = int(hra[1])//60
    min = int(hra[1])%60
    print(f"{hra[0]}, {hod}h {min}min")
