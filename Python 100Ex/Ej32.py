# Escribir un programa que cree la variable L y le asigne la lista 
# [3,6,9,12,15,18,21,24]. Luego, crear una nueva lista L1 mediante una
# comprensión de lista que contenga los números de L divididos por 3. El 
# programa debe mostar la lista L1 en la consola

L = [3,6,9,12,15,18,21,24]
L1 = []

for l in L: 
    if l%3 == 0:
        L1.append(l)

print(L1)

# or 

L1 = [l/3 for l in L]
print(L1)