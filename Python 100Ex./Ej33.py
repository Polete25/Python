# El programa para crear la variable L y asignarle la lista
# [-6,5,-3,-1,2,8,-3.6], luego crear una nueva lista L1 usando comprensión de 
# lista con los núemroes de L que son estricatamente mayores que 0 y finalmente 
# mostrar la lista L1 en la consola.

L = [-6,5,-3,-1,2,8,-3.6]
L1 = []

for l in L: 
    if l > 0:
        L1.append(l)
        
print(L1)

# or 

L1 = [l for l in L if l > 0]
print(L1)