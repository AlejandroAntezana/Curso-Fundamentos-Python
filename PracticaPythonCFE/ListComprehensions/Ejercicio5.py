'''
**Vocales en una Frase:**
   Dada una frase, crea una lista que contenga todas las vocales de la frase.
'''

frase= "extrovertida"
vocales = "aeiou"

lista_con_vocales = [letra for letra in frase.lower() if letra in vocales]

print(lista_con_vocales)