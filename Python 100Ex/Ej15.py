# Escribir un programa que cree la lista L asignándole el valor [1,2,3,4,5,6,7
# ,8,9,10] y luego crear una lista L1 que recupera un elemento de cada tres en
# la lista L. En este caso, debemos obtener al final la siguiente lista:
# [1,4,7,10]

L1 = [1,2,3,4,5,6,7,8,9,10]
L2 = []
i = 0
for l1 in L1:
    if i%3 == 0:
        L2.append(l1)
    i += 1

print(L2)