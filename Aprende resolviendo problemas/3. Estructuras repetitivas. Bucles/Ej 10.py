# Escribe un programa que muestre el valor máximo escrito por el usuario. El 
# programa debe dejar de ejecutarse una vez que el usuario introduzca un 0.

numero = -999999999
numeromax = -999999999
while numero != 0:
    numero = int(input("Introducir número: "))
    if numero > numeromax:
        numeromax = numero

print(f"Máximo: {numeromax}")
