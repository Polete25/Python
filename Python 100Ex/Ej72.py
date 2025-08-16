# Escribe un programa que permita almacenar en una lista L todos los enteros 
# positivos de tres dígitos de la forma abc tal que, para cada entero, la suma 
# de sus dígitos a+b+c sea un divisor del producto de sus dígitos a*b*c. 
# El programa debe mostrar al final la lista que contiene estos enteros. Por 
# ejemplo: el número 514 cumple con esta propiedad, 5+1+4 = 10 es un divisor de 
# 5*1*4 = 20.

L = list()

for l in range(100,1000):
    numero = str(l)
    a = 1
    b = 0
    for n1 in  numero:
        n1 = int(n1)
        a = n1 * a
    for n2 in numero:
        n2 = int(n2)
        b += n2
    if a != 0 and a % b == 0:
        L.append(l)
        
print(L)
