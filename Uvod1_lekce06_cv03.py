# Registrace

# Založte si program registrace.py. Program nechá uživatele, aby si zvolil uživatelské jméno a heslo. Heslo jej nechejte zadat dvakrát a ověřte, že jej uživatel zadal dvakrát stejně. V opačném případě vypište varování, že hesla nejsou stejná. Při prvním zadávání ověřte, že heslo je bezpečné, což v tomto případě znamená, že je delší než 8 znaků.
print("\nRegistrace účtu.\n")
heslo_1 = input("Zadejte své heslo (minimálně 8 znaků): ")
if len(heslo_1) < 8:
    print("Vámi zvolené heslo je příliš krátké. Registraci nelze uskutečnit.\n")
    exit()
else:
    pass
heslo_2 = input("Zadejte znovu své heslo (musí se shodovat s předchozím): ")
if heslo_1 != heslo_2:
    print("Hesla nejsou stejná. Registraci nelze uskutečnit.\n")
    exit()
else:
    print("Registrace proběhla v pořádku.\n")

