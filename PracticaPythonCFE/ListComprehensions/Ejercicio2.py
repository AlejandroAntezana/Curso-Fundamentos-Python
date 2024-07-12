'''
**Números Pares:**
   Crea una lista que contenga los números pares del 1 al 20 utilizando list comprehension.
'''

lista_de_pares = [x for x in range(1, 21) if x % 2 == 0]

print(lista_de_pares)