# Escribir una función Eltseparado(L) que tome como parámetro una lista L cuyos 
# elementos son 0 y 1, y separa los 0 de los 1 colocando los 0 al principio del 
# arreglo y los 1 a continuación. 

def eltseparado(L):
    n0 = L.count(0)
    n1 = L.count(1)
    L = []
    i = 0
    while i < n0:
        L.append(0)
        i += 1
    i = 0
    while i < n1:
        L.append(1)    
        i += 1
        
    return L

print(eltseparado([0,1,0,1,1,0,0,1,0,1]))
print(eltseparado([1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1]))
    