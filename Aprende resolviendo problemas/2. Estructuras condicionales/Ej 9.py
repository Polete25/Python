# Escribe un programa que calcule el múltiplo de siete basado en la entrada del 
# usuario.

numero = int(input("Introduce un número: "))

if numero%7 == 0:
    print(f"{numero} es multiple de 7.")
else:
    print(f"{numero} no es multiplo de 7")