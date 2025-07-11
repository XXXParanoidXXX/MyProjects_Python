Lista_Fruta = []
# Adicionando elementos à lista com laço de repedição
for i in range(3):
    fruta = input("Digite o nome de uma fruta: ")
    Lista_Fruta.append(fruta)
# Exibindo a lista
print("Primeira lista: ", Lista_Fruta)
# Outra forma de adicionar elementos à lista
Lista_Fruta2 = []
# Adicionando elementos diretamente
Lista_Fruta2.append("Limão")
Lista_Fruta2.append("Acerola")
Lista_Fruta2.append("Laranja")
# Exibindo a lista
print("Segunda lista: ", Lista_Fruta2)

#Agora, fazendo uma matriz com as duas listas
Matriz_Frutas = [Lista_Fruta, Lista_Fruta2]
# Exibindo a matriz
print("Matriz de Frutas: ", Matriz_Frutas)


