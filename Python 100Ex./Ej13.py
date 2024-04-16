# Escribir las instrucciones que permiten craer la lista L asignándole los 
# valores [3,2,2,1,9,1,2,3,7], luego calcular el número de apariciones del
# numero 1 en la lista L.

L = [3,2,2,1,9,1,2,3,7]

print(L.count(1))

c1 = 0

for l in L:
    if l == 1:
        c1 += 1
        
print(c1)