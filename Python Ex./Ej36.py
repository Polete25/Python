# Escribe un programa que calcula la suma de los dígitos de un número.
# El programa debe mostrar el resultado en la consola.

def sumardig(n):
    x = [int(a) for a in str(n)]
    return sum(x)

print(sumardig(3018))

# or 

numero = 3018

numero = str(numero)

suma = 0

for digit in numero:
    suma += int(digit)
    
print(suma)
    