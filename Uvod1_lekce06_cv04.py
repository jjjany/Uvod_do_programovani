# Přestupný rok

# Napište program, který po zadání kalendářního roku vypíše, zda jde o rok přestupný, či nikoliv. Letopočet je přestupný, pokud je dělitelný čtyřmi. Roky, které jsou dělitelné 100 jsou ovšem přestupné pouze tehdy, jsou-li zároveň dělitelné 400.

print("\nKterý rok je přestupný?\n")
rok = int(input("Zadej rok: "))
if rok%4 == 0:
    if rok%100 == 0:
        if rok%400 == 0:
            vyrok = "je"
        else:
            vyrok = "není"
    else:
        vyrok = "je"
else:
    vyrok = "není"
print(f"Rok {rok} {vyrok} přestupný.\n")
