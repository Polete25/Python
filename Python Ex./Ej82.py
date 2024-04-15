# Escribir una función esCirculoPrimo(numero) que toma como parámetro un número
# entero numero y verifica si es un número circular primo. La función devuelve 
# True si el número pasado como parámetro es un número circular primo y False en
# caso contrario. Recordatorio: un número es un núero circular primo si la 
# rotación de sus dígitos son números primos. Por ejemplo, el número 197 es un 
# número circular primo ya que 197, 971 y 719 son números primos (el primer 
# dígito de 197 se mueve al final del número y obtenemos 971, luego el 9 al 
# final de 971 y obtenemos 719) Otros números circulares primos: 19391, 19937,
# 71, 37, 31, 9377, etc. Indicación: se recomienda implementar una función
# esPrimo(numero) que verifique si un número primo, y luego usarla en 
# esCirculoPrimos(numero). 

def esPrimo(numero):
    numero = int(numero)
    for r in range(2,numero-1):
        if numero%r == 0:
            return False
    return True

def esCirculoPrimo(numero): 
    numero = str(numero)
    l = len(numero)
    numeros_circular = list()
    
    for i in range(l):
        numeros_circular.append(numero[i:] + numero[:i]) 
        
    for numero in numeros_circular:
        if not esPrimo(numero):
            return False
    
    return True
            
    
print(esCirculoPrimo(9377))
print(esCirculoPrimo(36))
        

    