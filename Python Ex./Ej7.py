# Escribir un programa que solicite al usuario su edad y la almacene en una 
# variable. El programa debe verificar si el usaurio tiene una edad mayo o menor
# a 18 años. Si la edad del usuario es mayor o igual a 18, entonces el programa
# debe imprimir "El usuaro es mayor de edad", de lo contrario debe imprimir
# "El usuario es menor de edad"

edad = int(input("Cual es su edad? "))

if edad >= 18:
    print("El usuario es mayor de edad.")
else:
    print("El usuario es menor de edad.")