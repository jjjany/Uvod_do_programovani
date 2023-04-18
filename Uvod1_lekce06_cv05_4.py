# Ruleta

# Na obrázku vidíte rozložení čísel na klasické Francouzské ruletě. Ruleta obsahuje čísla 0 - 36. Každé číslo s výjimkou nuly je buď sudé nebo liché a zároveň červené nebo černé. Pro čísla 1 až 10 a 19 až 28 platí, že lichá čísla jsou červená a sudá jsou černá. Pro zbytek platí obrácené pravidlo, tedy lichá jsou černá a sudá červená. Nula není ani lichá ani sudá, ani černá ani červená.
# Napište program, kterému uživatel zadá číslo a program odpoví jestli jde o číslo sudé nebo liché, černé nebo červené, nebo je to nula.

print("\nVítejte v Ruské ruletě!\n\nPo zadání čísla ti odpovím, zda je číslo liché, nebo sudé, červené, nebo černé.\n")
n = int(input("Zadej celé číslo od 0 do 36: "))
if (n >= 0) and (n <= 36):
    if n == 0:
        typ = "nula"
        barva = "zelená"
    elif n%2 == 0:
        typ = "sudé"
        if ((n >= 1) and (n <= 10)) or ((n >= 19) and (n <= 28)):
            barva = "černá"
        else:
            barva = "červená"
    else:
        typ = "liché"
        if ((n >= 1) and (n <= 10)) or ((n >= 19) and (n <= 28)):
            barva = "červená"
        else:
            barva = "černá"
else:
    print("Zadané číslo v Ruské ruletě není. Hra skončila.\n")
    exit()
print(f"Číslo {n} je {typ} a jeho barva je {barva}. Děkuji za vaši účast ve hře!\n")