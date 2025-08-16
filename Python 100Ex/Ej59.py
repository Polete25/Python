# Escribir una función unionLista(L1,L2,L3) que tome como parámetros tres listas 
# de enteros L1,L2 y L3 y devuelve una lista en orden ascendente que representa 
# la unión de estas tres listas sin duplicación de números.

def unionLista(L1,L2,L3):
    L4 = L1 + L2 + L3
    L4 = set(L4)
    L4 = sorted(L4)
    return L4

print(unionLista([3,6,9,3],[1,0,3],[12,6,0]))
print(unionLista([7,44,-3],[],[7,2,7]))
    