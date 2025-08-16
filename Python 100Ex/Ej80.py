# Escribir una función esUnPalindromo(numero) que tome como parámetro un número
# entero nbr y devuelva True si numero es un palíndromo y False si no lo es.
# Recordatorio: Un número palíndromo es un número natural mayor que 10, que 
# leído de izquierda a derecha o de derecha a izquierda, proporciona el mismo 
# número. Por ejemplo: los números 69596, 4231324, 212 son números palíndromos.

def isdigit(numero):
    numero = str(numero)
    left = 0
    right = len(numero) - 1
    
    while left < right:
        if numero[left] != numero[right]:
            return False
        left += 1
        right -= 1
    return True

print(isdigit(10))
print(isdigit(919))
        
        