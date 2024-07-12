'''
**Números Primos Menores a 50:**
   Crea una lista que contenga los números primos menores a 50.
'''
import math

def esPrimo(numero):
    if numero < 2:
        return False
    limite = round(math.sqrt(numero)) + 1
    for i in range(2, limite):
        if numero % i == 0:
            return False
    return True


lista_de_primos = [x for x in range(1, 51) if esPrimo(x)]
print(lista_de_primos)






