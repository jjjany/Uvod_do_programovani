# Největší prvek

# Napište cyklus, který projde zadaný seznam celých čísel a najde v něm největší hodnotu.
cisla = [-7, -3, -6, -5, 10, -7, -9, -8]

a = cisla[0]
for i in cisla:
    if i >= a:
        a = i
    else:
        pass
print(a) 
    