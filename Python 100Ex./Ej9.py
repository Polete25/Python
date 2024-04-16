# Escribir un programa en Python que prermita imprimir solo los números impares
# entre 10 y 20. Nota: es necesario crear dos versiones, una con el bucle for
# y la otra con el bucle while.

i = 10

while i < 21:
    if i%2 != 0:
         print(i)
         i += 1
    else:
        i += 1
        
for i in range(10,21):
    if i%2 != 0:
         print(i)
         i += 1
    else:
        i += 1
    