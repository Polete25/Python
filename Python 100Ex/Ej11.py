# Escribir la instruccion que permita crear una lista de números pares del 1 al
# 10 con una comprensión de lista.

l = [i for i in range(1,11) if i%2 == 0]
print(l)