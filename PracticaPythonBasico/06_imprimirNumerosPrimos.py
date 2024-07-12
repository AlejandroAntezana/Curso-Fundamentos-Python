'''
Ejercicio 6: Números Primos
Escribe un programa que imprima los números primos del 1 al 20.
'''
import math


# Creamos una función que determina si un número es primo o no
def esPrimo(numero):
    if numero < 2:
        return False
    limite = round(math.sqrt(numero)) + 1
    for i in range(2, limite):
        if numero % i == 0:
            return False
    return True


for i in range(1, 21):
    if esPrimo(i):
        print(f"El número {i} es Primo")
