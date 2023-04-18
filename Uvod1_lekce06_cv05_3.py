# Gymnázium

# Modifikujme si předchozí příklad. Horší známku z matematiky může student kompenzovat tím, že uspěje v matematické olympiádě. Přidejte tedy dotaz, zda se uchazeč zúčastnil okresního kola matematické olympiády. Pokud ano, bude mu zkouška odpuštěna, i kdyby jeho známka z matematiky byla horší. Požadavek na celkový průměr známek je však třeba stále dodržet.

# Otázka může vypadat například takto:

# input("Zúčastnil ses okresního kola krajské olympiády? [a/n] ")

# Pokud se student olympiády zúčastnil, odpoví a.

print(("\nInformace pro uchazeče o studium na našem gymnáziu.").upper(),"\n\nZjistěte, zda pro přijetí budete muset absolvovat přijímací zkoušku.")

matematika = int(input("Zadejte svoji známku z matematiky na posledním vysvědčení: "))
prumer = float(input("Zadejte průměr ze všech známek na posledním vysvědčení: "))
olympiada = input("Zúčastnil*a jste se okresního kola krajské olympiády? [ano/ne]: ")
olympiada = olympiada.lower() == "ano"

if ((matematika <= 2) or olympiada) and (prumer < 1.8):
    print("\nPřijmeme vás bez přijímací zkoušky.\n")
else:
    print("\nMusíte splnit přijímací zkoušku.\n")
