'''
**Longitudes de Palabras:**
   Dada una lista de palabras, crea una lista que contenga las longitudes de cada palabra.
'''
lista_de_palabras = ["el", "Ale", "ojota", "libros", "comer", "ta", "mamucha", "estudiar", "comprehensions"]

longitudes_de_palabras = [len(palabra) for palabra in lista_de_palabras]
print(longitudes_de_palabras)