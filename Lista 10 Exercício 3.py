# 3. Considerando duas matrizes A e B de ordem  3 (3x3),
#   a. Preenche-las  com números aleatórios entre 1 e 9.
#   b. Exibir as matrizes A e B.
#   c. Construir a Matriz C, resultado da soma das matrizes A e B.
#   d. Exibir a matriz C

import random
from tracemalloc import start;

def RandomMatriz(matriz):
  for x in range(0, len(matriz)):
    for y in range(0, len(matriz[x])):
      matriz[x][y] = random.randint(1, 9);
  return matriz;

def PrintMatriz(matriz):
  for x in range(0, len(matriz)):
    print();
    for y in range(0, len(matriz[x])):
      print(matriz[x][y], end=" ");

def SomaMatrizes(matrizA, matrizB):
  matrizC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
  for x in range(0, len(matrizA)):
    for y in range(0, len(matrizA[x])):
      matrizC[x][y] = matrizA[x][y] + matrizB[x][y];
  return matrizC;

matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];

matriz1 = RandomMatriz(matriz1);
matriz2 = RandomMatriz(matriz2);

print("Matriz 1: ");
PrintMatriz(matriz1);
print("\nMatriz 2: ");
PrintMatriz(matriz2);

print("\nMatriz 3: (Que é = Matriz 1 + Matriz 2)");
PrintMatriz(SomaMatrizes(matriz1, matriz2));

input()