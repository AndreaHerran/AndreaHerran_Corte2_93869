import random as r

lista = [ ]
for i in range(10):
    numero = r.randint(1, 50)
    lista.append(numero)

def mayor(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return print(f"El número mayor de la lista es: {max}")

def primos(lista):
    primos = []
    for num in lista:
        primo = True
        if num < 2:
            primo = False
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            primos.append(num)
    if primos:
        print("Los números primos de la listas son; ", primos)
    else:
        print("No hay números primos en la lista")

print(f"La lista aleatoria es: {lista}")
print(primos(lista))
print(mayor(lista))
