# En este ejercicio, retomaremos la solución del ejercicio 37 que consiste en 
# escribir una función natural N positivo y devuelva el elemento de índice N
# de la sucesión de Fibonacci. 

def fun(N):
    if len(N) == 0:
        return 0
    return N[0] + fun(L[1:])

fun([3,2,6,9,-1,5])