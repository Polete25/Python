# Escribir una función llamada posicionEltLista(L,x) que tome como parámetro una
# lista de elementos L y un elemento x, y devuelva el índice (o los índices) 
# donde se encuentrael elemento x en la lista L. La función debe devolver una 
# lista de índices. Si el elemento x no se encuentra en la lista L, el programa 
# mostrará en la consola: "El elemento x no está e la lista L"

def posicionEltLista(L,x):
    indi = list()
    index = 0
    for l in L:
        if x == l:
            indi.append(index)
        index += 1
    return indi

print(posicionEltLista([1,2,3,6,8,7,3],3))