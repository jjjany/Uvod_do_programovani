# Ověřování hesla

# Ověřování hesla se někdy dělá tak, že se vás systém ptá pouze na některé jeho znaky. Napište program, který má uloženo heslo, které musí uživatel zadat. Pak se jej postupně zeptejte například na druhý, pátý a sedmý znak hesla. Propusťte uživatele pouze tehdy, zadá-li všechny tyto znaky správně.
heslo = str(input("\nZadej heslo (miniláně 8 zanků): "))
chyba = "To není správně! Heslo nebylo ověřeno!\n"
znak2 = str(input("Zadej 2. znak z hesla: "))
if znak2 != heslo[1]:
    print(chyba)
    exit()
else:
    znak5 = str(input("Zadej 5. znak z hesla: "))
    if znak5 != heslo[4]:
        print(chyba)
        exit()
    else:
        znak7 = str(input("Zadej 7. znak z hesla: "))
        if znak7 != heslo[6]:
            print(chyba)
            exit()
        else:
            print("Heslo bylo ověřeno!\n")
