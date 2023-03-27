import random as r

lista = [ ]
for i in range(10):
    numero = r.randint(1, 50)
    lista.append(numero)
print(lista)
def mayor(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max
print(mayor(lista))
def primos(lista):
    primos = []
    if lista < 2:
        print('no es primo')
    for i in range(2, lista):
        pass


