'''
**Números Múltiplos de 3 y 5:**
   Crea una lista que contenga los números del 1 al 50 que son múltiplos de 3 o 5.
'''

lista_con_multiplos = [num for num in range(1, 51) if (num%3==0 or num%5==0)]
print(lista_con_multiplos)