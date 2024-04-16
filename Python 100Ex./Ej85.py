# Escribir una función busquedaDicotomica(L,elt) que toma como parámetros una 
# lista L ordenada en orden ascendente y un elemento elt. La función nos permite
# encontrar el elemento elt en la lista L mediante una búsqueda dicotómica. Si 
# el elemento es encontrado, entonces la función devuelve True, de lo contrario 
# devuelve False.

def busquedaDicotomica(L,elt):
    L.sort()
    while L:
        idx_medio = len(L) // 2
        if elt == L[idx_medio]:
            return True
        elif elt < L[idx_medio]:
            L = L[:idx_medio]
        else:
            L = L[idx_medio:]
    return False

print(busquedaDicotomica([6,9,15,36,41,43,47],41))
print(busquedaDicotomica([-9,-1,3,4,7,11],0)) # no funciona.. 