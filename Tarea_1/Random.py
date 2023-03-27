import random as r
def Aleatorio():
    numeros = []
    while len(numeros) < 10:
        num = r.randint(100, 120)
        if num not in [110, 115, 119]:
            numeros.append(num)
    pares = []
    impares = []
    for i in range(10):
        if i % 2 == 0:
            pares.append(numeros[i])

        else:
            impares.append(numeros[i])
    for i in range(5):
        print(pares[i], '\n', impares[i])
print(Aleatorio())


