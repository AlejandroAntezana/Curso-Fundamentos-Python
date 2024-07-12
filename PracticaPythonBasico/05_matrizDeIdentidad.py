'''
Ejercicio 5: Matriz de Identidad
Crea una función que tome un número n como argumento y devuelva una matriz de identidad de tamaño n x n.
'''

tam_matriz = int(input("Ingrese un numero => "))
print("La matriz nxn es: ")

for i in range(1, tam_matriz + 1):
    for j in range(1, tam_matriz + 1):
        print("1" if i == j else "0", end=" ")
    print("")


