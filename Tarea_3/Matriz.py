import random as rand

matriz=[]
for i in range(5):
    matriz.append([])
    for j in range(10):
        num = rand.randint(1,10)
        matriz[i].append(num)

max = matriz[0][0]
pos = (0, 0)
for i in range(5):
    for j in range(10):
        if matriz[i][j] > max:
            max = matriz[i][j]
            pos = (i, j)

min = matriz[0][0]
posi = (0, 0)
for i in range(5):
    for j in range(10):
        if matriz[i][j] < min:
            min = matriz[i][j]
            posi = (i, j)

print(matriz)
print(f"El número más alto es {max} en la posición {pos}")
print(f"El número más bajo es {min} en la posición {posi}")

