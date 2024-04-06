# Escribe una función minimo(L) que tome una lista de enteros L como parámetro
# y devuelva el valor más pequeño.

def minimo(L):
    n = L[0]
    for l in L: 
        if l < n:
            n = l 
    return n

print(minimo([-9,2,4,1,8]))
print(minimo([-3,1,7,6,2,3]))

