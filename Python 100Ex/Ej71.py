# Escribir una función funcTrigo(x) que tome un número x como parámetro y 
# devuelva el resultado de la función f(x) = cos(x)*sin(x) + sin(x) + 8. Nota:
# en este ejercicio vamos a utilizar el módulo math.

import math

def funcTrigo(x):
    f = math.cos(x)*math.sin(x)+math.sin(x) + 8
    return f

print(funcTrigo(math.pi/4))
print(funcTrigo(math.pi))