# Soutěž

# Divadlo Pěst na oko pořádá soutěž o lístky na premiéru nového představení Zločin v podmínce. Pro účast v soutěži musí zájemce splnit následující dvě podmínky:

#     Sdílel alespoň 5 příspěvků divadla na sociálních sítích.
#     Letos navštívil(a) alespoň 5 představení.

# Současně platí, že soutěžit můžou všichni členové Klubu přátel Divadla Pěst na oko, i kdyby podmínky nesplnili.

# Tvým úkolem je vytvořit program, který se uživatele zeptá na všechny potřebné informace (stačí odpověď ano/ne) a vyhodnotí, zda se může zúčastnit soutěže.

print("\nDivadlo Pěst na oko pořádá soutěž o lístky na premiéru nového představení Zločin v podmínce. Pro účast v soutěži musí zájemce splnit naše podmínky. Odpověz na otázky a zjisti, zda se soutěže můžeš zúčastnit.\n")
navstevy = input("Navštívil*a jsi letos alespoň 5 představení v našem divadle? [ano/ne] ")
sdileni = input("Sdílel*a jsi alespoň 5 příspěvků našeho divadla na sociálních sítích? [ano/ne] ")
klub = input("Jsi členkou / členem Klubu přátel Divadla Pěst na oko? [ano/ne] ")
navstevy = navstevy.lower() == "ano"
sdileni = sdileni.lower() == "ano"
klub = klub.lower() == "ano"

if (navstevy and sdileni) or klub:
    print("\nPodmínky soutěže byly splněny. Můžeš se zúčastnit.\n")
else:
    print("\nJe nám líto, nesplnil*a jsi podmínky soutěže. Soutěže se nemůžeš zúčastnit.\n")
