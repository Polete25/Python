# Ecribir el código de la función sumaSublista(L,i,j) que toma 3 parámetros: una
# lista L, un índice de inicio de cálcuo i y un índice de fin de cálculo j. La 
# función debe devolver la suma de los números que se encuentran entre los 
# índices i y j de la lista,

def sumaSublista(L,i,j):
    suma = 0
    for n in range(i,j+1):
        suma += L[n]
    return suma

print(sumaSublista([4,10,12,16,18],2,4))
print(sumaSublista([2,4,6,8,10,12],0,2))

# or 

def sumaSublista(L,i,j):
    Lij = L[i:j+1]
    suma = 0
    for elt in Lij:
        suma += elt
    return suma

print(sumaSublista([4,10,12,16,18],2,4))
print(sumaSublista([2,4,6,8,10,12],0,2))
