# Escribe un programa que pida un número. Luego, el programa le dirá si 
# esenumero es negativo, positivo o cero.

numero = int(input("Escribe un número:"))
if numero == 0:
    print("Cero")
elif numero < 0:
    print("Es un número negativo.")
else:
    print("Es un número positivo.")
    
    