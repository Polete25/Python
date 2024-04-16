# Escirbe un programa que nos diga si un carácter introdcuido por el usuario es
# una vocal o no.

caracter = input("Introduce una letra:")
vocales = ['a','e','i','o','u']

if caracter.lower() in vocales:
    print("Es una vocal.")
else: 
    print("No es una vocal.")