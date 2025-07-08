Nota1 = float(input("Nota 1: "))
Nota2 = float(input("Nota 2: "))
Nota3 = float(input("Nota 3: "))
Nota4 = float(input("Nota 4: "))

Media = (Nota1 + Nota2 + Nota3 + Nota4)/4

print("A média final é igual a:", Media)

if Media >= 7:
    print("Aprovado")
elif Media >= 5:
    print("Recuperação")
else:
    print("Reprovado") 