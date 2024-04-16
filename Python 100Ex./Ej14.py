# Escribir las instrucciones que permiten crear una lista vacía L y agregarle 
# los enteros 10,25,30,45,90 y las cadenas de caracteres 'ab', 'cd', 'ef'.

# Metodo 1:

L = []
L += [10,25,30,45,90,"ab","cd","ef"]
print(L)

# Metodo 2:

L = []
add = [10,25,30,45,90,"ab","cd","ef"]
for e in add:
    L.append(e)
print(L)