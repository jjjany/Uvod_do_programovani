# Gymnázium

# Matematické gymnázium nabízí aplikaci, která sděluje informaci o povinnosti vykonání přijímací zkoušky. Požádejte uživatele o zadání známky z matematiky a průměru všech známek na posledním vysvědčení. Pokud má zájemce průměr známek nižší než 1.8 a z matematiky nejhůře dvojku, vypište text: "Přijmeme vás bez přijímací zkoušky.". V opačném případě vypište "Musíte splnit přijímací zkoušku.".

print(("\nInformace pro uchazeče o studium na našem gymnáziu.").upper(),"\n\nZjistěte, zda pro přijetí budete muset absolvovat přijímací zkoušku.")

matematika = int(input("Zadejte svoji známku z matematiky na posledním vysvědčení: "))
prumer = float(input("Zadejte průměr ze všech známek na posledním vysvědčení: "))

if (matematika <= 2) and (prumer < 1.8):
    print("\nPřijmeme vás bez přijímací zkoušky.\n")
else:
    print("\nMusíte splnit přijímací zkoušku.\n")
