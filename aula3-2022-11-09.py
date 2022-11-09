print("inicio aula 3 (09/11/2022)")

contador = 1
#exibir de 1 a 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 #contador +=1


# Laço for (python for = for each)
fruta = "morango"
print("Segue uma fruta da primeira lista: ")
print(fruta)

#Lista
frutas = ["morango", "laranja", "pêra"]

#quero exibir apenas a 3ª fruta "Vetores"
print("A terceira fruta da segunda lista é: ")
print(frutas[2])

#exibir quantas frutas tem na minha lista
print("Segue quantas frutas tem na segunda lista: ")
print(len(frutas))

# Incluir fruna na lista
frutas.append("manga")

#ver a fruta acrescentada
print("A nova fruta acrescentada é: ")
print(frutas[3])
print("")
#ver as frutas
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print("")
frutas.append("uva") #Acrescentando fruta
i = 0
while(i<len(frutas)):
  print(frutas[i])
  i = i+1

