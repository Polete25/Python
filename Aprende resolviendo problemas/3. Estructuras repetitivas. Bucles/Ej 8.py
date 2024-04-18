# Escribe un programa que muestre números impares del 1 al 100.

for x in range(101):
    if x % 2 != 0:
        print(f"{x} ", end=" ")