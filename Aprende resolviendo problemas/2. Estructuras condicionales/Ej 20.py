# Escribe un programa que calcule el año bisiesto basado en la entradad del 
# usuario.

anyo = int(input("Introduce un año: "))

if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo & 400 == 0):
    print(f"{anyo} es un año bisiesto.")
else:
    print(f"{anyo} no es un año bisiesto.")