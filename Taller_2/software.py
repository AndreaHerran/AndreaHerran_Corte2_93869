import csv
def leer_datos(archivo):
    datos = []
    with open(archivo, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos
def organizar_paises(datos):
    paises = []
    for fila in datos:
        pais = fila[4]
        if pais not in paises:
            paises.append(pais)
    paises.sort()
    return paises
def nombre_pais(paises, numero_pais):
    if numero_pais >= 1 and numero_pais <= len(paises):
        return paises[numero_pais -1]
def empresa_mayor_empleados(datos, paises, nombre_pais):
    empresa_mayor_empleados = None
    max_empleados = -1
    for fila in datos:
        if fila[4] == nombre_pais:
            empleados = int(fila[8])
            if empleados > max_empleados:
                max_empleados = empleados
                empresa_mayor_empleados = fila
    return empresa_mayor_empleados
def empresa_menor_empleados(datos, paises, nombre_pais):
    empresa_menor_empleados = None
    min_empleados = float('inf')
    for fila in datos:
        if fila[4] == nombre_pais:
            empleados = int(fila[8])
            if empleados < min_empleados:
                min_empleados = empleados
                empresa_menor_empleados = fila
    return empresa_menor_empleados
def calcular_promedio_empleados(datos, paises, nombre_pais):
    total_empleados = 0
    num_empresas = 0
    for fila in datos:
        if fila[4] == nombre_pais:
            total_empleados += int(fila[8])
            num_empresas += 1
    if num_empresas > 0:
        promedio_empleados = total_empleados / num_empresas
        return promedio_empleados
    else:
        return None
def obtener_num_empresas(datos, paises, nombre_pais):
    num_empresas = 0
    for fila in datos:
        if fila[4] == nombre_pais:
            num_empresas += 1
    return num_empresas
archivo_csv = "organization_data.csv"
datos = leer_datos(archivo_csv)
paises = organizar_paises(datos)
numero_pais = int(input("Indice del país de busqueda: ".format(len(paises))))

nombre_pais = nombre_pais(paises, numero_pais)
if nombre_pais is not None:
    print("País:", nombre_pais, "\n")

    empresa_mayor_empleados = empresa_mayor_empleados(datos, paises, nombre_pais)
    if empresa_mayor_empleados is not None:
        print("Empresa con mayor # de empleados:")
        print("Empresa:", empresa_mayor_empleados[2])
        print("Website:", empresa_mayor_empleados[3])
        print("Descripción:", empresa_mayor_empleados[5])
        print("Fundación:", empresa_mayor_empleados[6])
        print("Industria:", empresa_mayor_empleados[7])
        print("# Empleados:", empresa_mayor_empleados[8], "\n")

    # Obtener los datos de la empresa con menor número de empleados
    empresa_menor_empleados = empresa_menor_empleados(datos, paises, nombre_pais)
    if empresa_menor_empleados is not None:
        print("Empresa con menor # de empleados:")
        print("Empresa:", empresa_menor_empleados[2])
        print("Website:", empresa_menor_empleados[3])
        print("Descripción:", empresa_menor_empleados[5])
        print("Fundación:", empresa_menor_empleados[6])
        print("Industria:", empresa_menor_empleados[7])
        print("# Empleados:", empresa_menor_empleados[8],"\n")

    # Calcular el valor promedio del número de empleados
    promedio_empleados = calcular_promedio_empleados(datos, paises, nombre_pais)
    if promedio_empleados is not None:
        print("Promedio empleados: {:.2f}".format(promedio_empleados))

    num_empresas = obtener_num_empresas(datos, paises, nombre_pais)
    print("Cantidad de empresas:", num_empresas)
else:
    print("Error: Número de país inválido.")

