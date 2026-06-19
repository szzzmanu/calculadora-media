nota1 = float(input("Líder Matutino: "))
nota2 = float(input("Vice Matutino: "))
media_mat = (nota1 + nota2) / 2

nota3 = float(input("\nLíder Vespertino: "))
nota4 = float(input("Vice Vespertino: "))
media_ves = (nota3 + nota4) / 2

nota5 = float(input("\nLíder Noturno: "))
nota6 = float(input("Vice Noturno: "))
media_not = (nota5 + nota6) / 2

print("\n----- MÉDIAS DAS TURMAS -----")
print("Matutino:", media_mat)
print("Vespertino:", media_ves)
print("Noturno:", media_not)

if media_mat > media_ves and media_mat > media_not:
    print("\nMaior média: Matutino")
elif media_ves > media_mat and media_ves > media_not:
    print("\nMaior média: Vespertino")
else:
    print("\nMaior média: Noturno")