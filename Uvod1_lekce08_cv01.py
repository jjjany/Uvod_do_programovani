# Seznam hodnocení

# Mějme seznam hodnocení divadelní hry Plyšáci na útěku , který vypadá takto:

hodnoceni = [7, 9, 6, 7, 9, 8]

#     a) Vytvořte program, který projde tento seznam a vypíše každé hodnocení na nový řádek.
for hodnota in hodnoceni:
    print(hodnota)

#     b) Upravte program tak, aby vypisoval výstup v tomto formátu

# 7/10
# 9/10
# 6/10
# 7/10
# 9/10
# 8/10
for hodnota in hodnoceni:
    print(f"{hodnota}/10")
