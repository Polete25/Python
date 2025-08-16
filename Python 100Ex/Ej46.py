# Escribe una función divisor(n) que tome un entero n como parámetro y devuelva 
# una lista que contenga todos los divisores positivos de n en orden ascendente.

def divisor(n):
    L = list()
    for i in range(1,n+1):
        if n%i == 0:
            L.append(i)
    return L

print(divisor(3))
print(divisor(9))
