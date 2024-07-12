'''
**Palabras que Comienzan con "A":**
   Dada una lista de palabras, crea una lista que contenga las palabras que comienzan con la letra "A".
'''

lista_de_palabras = ["el", "ale", "ojota", "libros", "comer", "ta", "mamucha", "estudiar", "comprehensions", "avion"]

lista_con_condicion = [palabra for palabra in lista_de_palabras if palabra[0] == "a"]

print(lista_con_condicion)