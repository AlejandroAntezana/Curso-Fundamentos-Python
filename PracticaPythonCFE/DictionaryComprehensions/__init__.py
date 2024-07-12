'''
1.Diccionario de Cuadrados:
Crea un diccionario que contenga los primeros 5 números naturales como claves y sus cuadrados como valores.

2.Diccionario de Longitudes:
Dada una lista de palabras, crea un diccionario que asocie cada palabra con su longitud.

3.Diccionario de Números Pares:
Crea un diccionario que contenga los números del 1 al 10 como claves y True si son pares y False si son impares como valores.

4.Diccionario de Iniciales:
Dada una lista de nombres, crea un diccionario que asocie cada nombre con su inicial.

5.Diccionario de Palabras con "a":
Dada una lista de palabras, crea un diccionario que asocie cada palabra que contiene la letra "a" con su longitud.
'''
text = "sasas"

#Ejercicio 1
dict_cuadrados = {clave: clave**2 for clave in range(1, 6)}
print(dict_cuadrados)

#Ejercicio 2
lista_de_palabras = ["el", "ale", "ojota", "libros", "comer", "ta", "mamucha", "estudiar", "comprehensions"]
dict_longitudes = {palabra: len(palabra) for palabra in lista_de_palabras}
print(dict_longitudes)

#Ejercicio 3
dict_pares_impares = {num: num % 2 == 0 for num in range(1, 6)}
print(dict_pares_impares)

#Ejercicio 4
lista_de_nombres = ["Ale", "Tati","Florencia","Lorena", "Marcia","Camila","Ernesto"]
dict_de_nombres = {inicial[0]: inicial for inicial in lista_de_nombres}
print(dict_de_nombres)

#Ejercicio 5
dict_de_palabras = {palabra: len(palabra) for palabra in lista_de_palabras if "a" in palabra}
print(dict_de_palabras)

