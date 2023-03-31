#2. Considere uma matriz 4x4 de valores inteiros:
#a) Preencher a matriz com números aleatórios na faixa de 1 a 15.

#Criando a matrix 4x4

import random

m=[]

for lin in range(4): #definir 4 linhas
    linha = []
    for col in range(4): #definindo uma linha com 4 números aleatórios
        linha.append(random.randint(1,15))
    m.append(linha)

#Exibindo a matriz

for lin in range(len(m)):
    for col in range (len(m[0])):
        print(m[lin][col], end=" ")
    print()

#b) Calcular e exibir a média aritmética dos valores da matriz.

soma = 0

for lin in range(len(m)):
    for col in range (len(m[0])):
        soma = soma + m[lin][col]

media = soma / 16

print(f"Média = {media}")

#c) Criar e exibir uma lista com os valores que são menores que a média dos valores da matriz.

lista = []

for lin in range(len(m)):
    for col in range (len(m[0])):
        if m[lin][col] < media:
            lista.append(m[lin][col])
print(f"Valores menores que a média = {lista}")
    
#d) Calcular e exibir a soma dos elementos da diagonal principal

soma = 0

for lin in range(len(m)):
    for col in range (len(m[0])):
        if lin == col:
            soma = soma + m[lin][col]

print(f"Soma dos elementos da diagonal principal = {soma}")


#e) Calcular e exibir a soma dos elementos da diagonal secundária

soma = 0

for lin in range(len(m)):
    for col in range (len(m[0])):
        if lin + col == len(m) - 1:
            soma = soma + m[lin][col]

print(f"Soma dos elementos da diagonal secundária = {soma}")

input()