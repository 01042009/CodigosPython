matriz=[]
total=0
import random
for i in range(3):
    fila=[]
    for j in range(3):
        fila.append(i)
        i = random.randint(1, 100)
    matriz.append(fila)
#mostar la matriz
for f in matriz:
    print(f)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        total += matriz[i][j]
print("suma es :",total)