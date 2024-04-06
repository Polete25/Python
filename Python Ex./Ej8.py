# Escribe un programa de Python que permita imprimir en la consola los números
# del 1 al 20. Nota: es necesario crear dos versiones, una con bucle for y la
# otra con el bucle while.

a = 1
while a <= 20:
    print(a)
    a += 1
    
r = range(1,21)    

for a in r:
    print(a)