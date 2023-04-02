import math;

# Solicitar al usuario que ingrese las dimensiones de las matrices
filas_mat1 = int(input("Ingrese el número de filas de la matriz 1: "))
columnas_mat1 = int(input("Ingrese el número de columnas de la matriz 1: "))
filas_mat2 = int(input("Ingrese el número de filas de la matriz 2: "))
columnas_mat2 = int(input("Ingrese el número de columnas de la matriz 2: "))


def sumar_matrices(mat1, mat2):
    # Verificar si las matrices tienen el mismo tamaño
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Las matrices no tienen el mismo tamaño"
    # Crear una matriz para el resultado
    resultado = []
    for i in range(len(mat1)):
        fila_resultado = []
        for j in range(len(mat1[0])):
            fila_resultado.append(mat1[i][j] + mat2[i][j])
        resultado.append(fila_resultado)
    return resultado

# Verificar si las matrices pueden ser sumadas y/o restadas
if filas_mat1 != filas_mat2 or columnas_mat1 != columnas_mat2:
    print("Las matrices no tienen el mismo tamaño para ser sumadas o restadas")
else:
    # Inicializar las matrices con ceros
    mat1 = [[0 for j in range(columnas_mat1)] for i in range(filas_mat1)]
    mat2 = [[0 for j in range(columnas_mat2)] for i in range(filas_mat2)]

    # Solicitar al usuario que ingrese los valores de la matriz 1
    print("Ingrese los valores de la matriz 1:")
    for i in range(filas_mat1):
        for j in range(columnas_mat1):
            mat1[i][j] = float(input(f"Valor en la fila {i+1}, columna {j+1}: "))

    # Solicitar al usuario que ingrese los valores de la matriz 2
    print("Ingrese los valores de la matriz 2:")
    for i in range(filas_mat2):
        for j in range(columnas_mat2):
            mat2[i][j] = float(input(f"Valor en la fila {i+1}, columna {j+1}: "))

    # Calcular y mostrar la suma de las matrices
    suma = sumar_matrices(mat1, mat2)
    print("La suma de las matrices es:")
    for fila in suma:
        print(fila)