#Criação de funções

preco = 1999.90

#Calcular 5% de imposto, guardae na variavel imposto e exibir na tela
#Calculo
imposto = preco * 0.05
#imprime na tela
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular imposto que calcula um imposto de 5% e retorna a quem pediu...
#Declaração da função
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Uso da Função para calcular_imposto
preco = 299
imposto =calcular_imposto(preco)
#exibir na tela
print(imposto)

#calcula agora com aliquota de 7%

valores = [1.99, 24.50, 78.27, 1515.5]
#Se eu quiser calcular o imposto destes quatro valores e exibir na tela " o imposto de...é..."(1º preço, ...)
for valor in valores:
 print(f"O imposto de {valor} é {calcular_imposto(valor)}")