# Escribe una función numeroOcurrencias(L) que tome como parámetro una lista L
# y devuelva una lista de tuplas donde cada tupla correspona a un elemento de la 
# lista L con su número de ocurrencias en la lista.

def numeroOcurrencias(L):
    tup = []
    for l in L:
        n = L.count(l)
        tup_etl = (l,n)
        if tup_etl not in tup:
            tup.append(tup_etl)
    return tup
    
print(numeroOcurrencias([-4,8,-3,2,1,2,7,9,-3,8,1]))
print(numeroOcurrencias(["a",3,4,"b","a",3]))