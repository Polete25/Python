# Escribe una función maximo(L) que tome una lista de enteros como parámetro y
# devuelva el mayor valor. Nota: La idea es no utilizar la función max() ya
# disponible en python

def maximo(L):
    m = L[0]
    for l in L:
        if l > m:
            m = l
    return m    

print(maximo([-9,2,4,1,8]))
print(maximo([-3,1,7,6,2,3]))