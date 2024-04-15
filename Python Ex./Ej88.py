# Escribir una función ordenamientoAsc(L) que toma como parámetro una lista de 
# enteros y permite ordenar la lista en orden creciente. La función debe 
# devolver la list L con los enteros ordenados de menor a mayor.

def ordenamientoAsc(L): 
    
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
                
    return L

print(ordenamientoAsc([6,1,9,-6,1,8,7]))
print(ordenamientoAsc([-3,5.3,2,7,1,2.3,9.5]))

