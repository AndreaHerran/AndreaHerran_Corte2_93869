import random as rand

matriz=[]
for i in range(5):
    matriz.append([])
    for j in range(10):
        num = rand.randint(1,10)
        matriz[i].append(num)