'''
Ejercicio 1: Suma de Números Pares
Escribe un programa que calcule la suma de los números pares del 1 al 50.
'''

total = 0
total2 = 0

# Recorriendo una "lista" y preguntado si son pares
for number in range(1, 51):
    if number % 2 == 0:
        total += number

# Tipo sumatoria
for number in range(0, 51, 2):  # Aca empieza en 0 y va de 2 en 2 => 0 - 2 - 4 - 6 ...
    total2 += number

print("La suma de los numeros pares del 1 al 50 es: ", total)
print("La suma de los numeros pares del 1 al 50 es: ", total2)
