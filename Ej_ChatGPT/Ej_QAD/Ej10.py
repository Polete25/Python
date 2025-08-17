# Calcular el factorial de un número (iterativo y recursivo).

def factorial(num: int) -> int:
    fact = 1
    for n in range(1,num+1):
        fact = fact * n

    return fact

print(factorial(5))