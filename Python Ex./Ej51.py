# Escribe una función llamada calculoFactorial(n) que permita calcular el 
# factorial de un número (en el sentido matemático) y devuelva el resultado 
# obtenido al final de este cálculo.

def calculoFactorial(n):
    tot = 1
    for i in range(1,n+1):
        tot = tot * i
        
    return tot

print(calculoFactorial(3))
print(calculoFactorial(9))
print(calculoFactorial(0))