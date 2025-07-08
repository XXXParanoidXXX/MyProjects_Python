Nome = input("Digite seu nome: ")
Sobrenome = input("Digite seu sobrenome: ")
Idade = input("Digite sua idade: ")

#print("O seu nome completo é " + str(Nome) + " " + str(Sobrenome) + " e a sua idade é " + str(Idade))
# A conversão para string é desnecessária, pois input já retorna uma string
# A função str() é redundante aqui, pois input já retorna uma string
# Portanto, podemos simplificar a linha de impressão
# A função print() já converte os valores para string automaticamente
# Assim, podemos remover as conversões desnecessárias

print("O seu nome completo é " + Nome + " " + Sobrenome + " e a sua idade é " + Idade)