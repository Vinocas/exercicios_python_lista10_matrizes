# 4. Considerando a matriz M , 5x5 faça,
#   a) Preencha a matriz com números aleatórios na faixa de 1 a 25
#   b) Calcule e exiba a soma dos elementos da primeira coluna;
#   c) Calcule e exiba o produto dos elementos da primeira linha;
#   d) Calcule e exiba a soma de todos os elementos da matriz;
#   e) Calcule e exiba a soma do diagonal principal;

import random;

def RandomMatriz(matriz):
  for x in range(0, len(matriz)):
    for y in range(0, len(matriz[x])):
      matriz[x][y] = random.randint(1, 25);
  return matriz;

def SomaColuna(matriz):
  soma = 0;
  for x in range(0, len(matriz)):
    soma += matriz[x][0];
  return soma;

def ProdutoLinha(matriz):
  produto = 1;
  for x in range(0, len(matriz)):
    produto *= matriz[0][x];
  return produto;

def SomaMatriz(matriz):
  soma = 0;
  for x in range(0, len(matriz)):
    for y in range(0, len(matriz[x])):
      soma += matriz[x][y];
  return soma;

def SomaDiagonalPrincipal(matriz):
  soma = 0;
  for x in range(0, len(matriz)):
    for y in range(0, len(matriz[x])):
      if x == y:
        soma += matriz[x][y];
  return soma;

M = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];

M = RandomMatriz(M);

print("A soma dos elementos da primeira coluna é: ", SomaColuna(M));
print("O produto dos elementos da primeira linha é: ", ProdutoLinha(M));
print("A soma de todos os elementos da matriz é: ", SomaMatriz(M));
print("A soma do diagonal principal é: ", SomaDiagonalPrincipal(M));

input()