# Tabuada.py
# Este programa exibe a tabuada de um número fornecido pelo usuário.
tabuada = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {tabuada}:")
for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}") 

# Fim do programa

#Outra forma de escrever o mesmo programa com mudança no loop
# Tabuada.py
# Este programa exibe a tabuada de um número fornecido pelo usuário.
tabuada = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {tabuada}:")
i = 1
while i <= 10:
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")
    i += 1