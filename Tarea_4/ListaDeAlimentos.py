def main():
    alimentos = {}
    alimentos_por_iva = {}
    with open("Alimentos.txt", "rt") as lista:
        lista.readline()
        for linea in lista:
            codigo, descripcion, tarifa_iva = linea.strip().split(",")
            alimentos[descripcion] = {"codigo": codigo, "tarifa_iva": float(tarifa_iva)}
            if tarifa_iva not in alimentos_por_iva:
                alimentos_por_iva[tarifa_iva] = []
            alimentos_por_iva[tarifa_iva].append(descripcion)
        print("Artículos organizados por valor del IVA:")
        for iva, alimento in alimentos_por_iva.items():
            print(f"Artículos de iva {tarifa_iva}% : {','.join(alimento)}")
    return alimentos
def calcular_valor_base_y_iva(precio_net, tarifa_iva):
    valor_base = precio_net / (1 + tarifa_iva)
    valor_iva = precio_net - valor_base
    return valor_base, valor_iva
while True:
    alimentos = main()
    nombre_producto = input("Ingrese el nombre del producto o escriba 'salir' para salir: ")
    if nombre_producto == "salir":
        break
    elif nombre_producto in alimentos:
        precio_net = float(input("Ingrese el valor neto del mercado actual: "))
        tarifa_iva = alimentos[nombre_producto]["tarifa_iva"]
        valor_base, valor_iva = calcular_valor_base_y_iva(precio_net, tarifa_iva)
        print("Valor base: $", round(valor_base, 2))
        print("Valor del IVA: $", round(valor_iva, 2))
    else:
        print("Producto no encontrado.")
