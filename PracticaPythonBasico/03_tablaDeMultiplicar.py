'''Ejercicio 3: Tabla de Multiplicar
Escribe un programa que solicite al usuario un número e imprima la tabla de multiplicar de ese número del 1 al 10.
'''

number = int(input("ingrese un numero => "))

print(f"La tabla de multiplicar del numero {number} es:")

for i in range(1,11):
    print(f"{number} * {i} = {number * i}")
