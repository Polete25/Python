# Escribe una función calcularSuma(L) que tome una lista de enteros L como 
# parámetro y devuelva la suma de los valores de lesa lista.

def calcularSuma(L):
    return sum(L)

print(calcularSuma([3,2,6,9,-1,5]))
print(calcularSuma([-3,-6,0,1,2,7]))

# or

def calcularSuma(L):
    tot = 0
    for l in L:
        tot += l 
    return tot

print(calcularSuma([3,2,6,9,-1,5]))
print(calcularSuma([-3,-6,0,1,2,7]))
