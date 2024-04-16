# Escribe una programa que compare dos usuarios en función de sus edades. El 
# programa debe decirnos quien es el más joven.

edad1 = int(input("Introducir edad del usuario 1: "))
edad2 = int(input("Introducir edad del usuario 2: "))

if edad1 > edad2:
    print("Usuario 2 es más joven")
elif edad1 == edad2:
    print("Tienen la misma esdad")
else:
    print("El usuario 1 es más joven")