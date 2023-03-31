# Construir e exibir uma matriz 2x4 de números inteiros quaisquer.

m = [[0,1,2,3],[4,5,6,7]]

for lin in range(len(m)): #linhas
    for col in range(len(m[0])): #colunas
        print(m[lin][col], end=" ")
    print()

input()