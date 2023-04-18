# Jednoduché podmínky

#     a) Založte si program prihlaseni.py. V tomto nechte uživatele zadat svoje uživatelské jméno a poté heslo. Pokud se heslo neshoduje s heslem simsalabim, vypište na výstup: "Vstup nepovolen"
# a zavolejte funkci exit(), aby uživatel neznalý hesla nemohl s programem dál pracovat.
uziv_jm = input("\nZadej své uživatelské jméno: ")
heslo = input("Zadej své heslo: ")

if heslo != "simsalabim":
    print("Vstup nepovolen!\n")
    exit()
else:
    pass

#     b) Na konec programu vlož příkaz, který se uživatele zeptá na věk. Pokud je uživatel starší 18 let, vypište na výstup:"Smíš vstoupit." 
# Pokud je mladší, vypiš: "Vstup povolen od 18 let."
vek = int(input("Kolik je ti let? Napiš svůj věk: "))

if vek >= 18:
    print("Smíš vstoupit.\n")
else:
    print("Vstup povolen od 18 let.\n")



