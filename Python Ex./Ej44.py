# Escribe una función longitud(L) que tome como parámetro una lsita de enteros L
# y devuelva el número de elementos de dicha lista.

def longitud(L):
    i = 0
    for l in L:
        i += 1
    return i

print(longitud([3,6,7,'2abde',[1,3,57],True]))
print(longitud([]))