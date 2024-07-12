'''
Ejercicio 10: Cálculo del Factorial
Escribe un programa que solicite al usuario un número e imprima su factorial.
'''
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

numero = int(input("Ingrese un numero para calcular su factorial => "))
numero = factorial(numero)
print(f"El factorial del numero ingresado es {numero}")