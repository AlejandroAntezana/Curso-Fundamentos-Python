'''
**Palabras Mayores a 3 Letras:**
   Dada una lista de palabras, crea una lista que contenga las palabras que tienen más de 3 letras.
'''

lista_de_palabras = ["el", "Ale", "ojota", "libros", "comer", "ta"]

lista_con_condicion = [palabra for palabra in lista_de_palabras if len(palabra)>3]

print(lista_con_condicion)