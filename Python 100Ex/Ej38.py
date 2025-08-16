# Escribe una fucnión eliminarDuplicados(L) que tome una lista enteros L como
# parámetro y devuelva la lista L sin elementos duplicados en orden ascendente.

def eliminarDuplicados(L):
    L1 = list(set(L))
    L1.sort()
    return L1
 
print(eliminarDuplicados([0,3,5,7,3,5,1,-1]))
print(eliminarDuplicados([0,5,9,10,3.2,1,-3]))

# or

def eliminarDuplicados(L):
    
    for l in L:
        c = L.count(l)
        if c > 1:
            for i in range(c-1):
                L.remove(l)
    L.sort()
    return L

 
print(eliminarDuplicados([0,3,5,7,3,5,1,-1]))
print(eliminarDuplicados([0,5,9,10,3.2,1,-3]))