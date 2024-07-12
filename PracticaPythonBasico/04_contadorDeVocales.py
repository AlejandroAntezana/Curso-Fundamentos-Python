'''
Ejercicio 4: Contador de Vocales
Escribe un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''
text = input("Ingrese una palabra => ")

text = text.lower()
count = 0
vocales = 'aeiou'

for leter in text:
    if leter in vocales:
        count += 1
print(f"La cantidad de vocales en la palabra {text} es {count}")