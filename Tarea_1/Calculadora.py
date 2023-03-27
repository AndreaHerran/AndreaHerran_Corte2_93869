import math as m
def calcular():
    funcion = input('ingrese funcion a realizar: ')
    valor = int(input('Ingrese el numero: '))
    if funcion == "sen":
        resultado = m.sin(valor)
    elif funcion == "cos":
        resultado = m.cos(valor)
    elif funcion == "tan":
        resultado = m.tan(valor)
    elif funcion == "exp":
        resultado = m.exp(valor)
    elif funcion == "log":
        resultado = m.log(valor)
    else:
        print("Función no válida. Las opciones son: seno, coseno, tangente, exponencial o logaritmo.")

    print(f"El resultado de {funcion} {valor} es: {resultado}")

print(calcular())

