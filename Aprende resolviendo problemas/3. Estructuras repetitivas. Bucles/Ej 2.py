# Escribe un programa que muestre una tabla de multiplicar basada en la entrada
# del usuario:

numero = int(input("Introduce un número: "))

for x in range(11):
    res = numero * x
    print(f"{numero} x {x} = {res}")
    