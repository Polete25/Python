# Escribe una fucnión medialista(L) que tome como parámetro una lista de enteros
# y devuelva la media de una lista L.

def medicaLista(L):
    i = 0
    suma = 0
    for l in L:
        suma += l
        i += 1
    return suma/i

print(medicaLista([1,2,3,4,5,6,7]))
print(medicaLista([3,0,-1,5,6,9,17]))

