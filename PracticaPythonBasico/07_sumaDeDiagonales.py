'''
Ejercicio 7: Suma de Diagonales
Crea una función que tome una matriz cuadrada como argumento y devuelva la suma de sus diagonales.
'''
def suma_diagonales(matriz):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    tam_matriz = len(matriz)

    for i in range(tam_matriz):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][tam_matriz - 1 - i]

    return suma_diagonal_principal, suma_diagonal_secundaria

# Ejemplo de uso
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [13, 8, 9]
]

resultado = suma_diagonales(mi_matriz)
print("Suma Diagonal Principal:", resultado[0])
print("Suma Diagonal Secundaria:", resultado[1])
