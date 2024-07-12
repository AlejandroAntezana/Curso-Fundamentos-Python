'''
Ejercicio 8: Palíndromo
Escribe un programa que verifique si una palabra ingresada por el usuario
es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

palabra = input("Ingrese una palabra => ")
palabra = palabra.lower()
palabra_invertida = palabra[::-1]

if palabra == palabra_invertida:
    print("La palabra ingresada es palindromo")
else:
    print("La palabra no es palindromo")