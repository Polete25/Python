# Escribir un programa que permita pedir una lista de enteros al usuario desde
# la consola el programa debe almacenar esta lista en una variable llamada 
# lista_usuario y mostrarla al final del programa. Nota: La función que tenemos 
# a nuestra disposición para interactuar con el usuario es input(), sin embargo,
# nos devuelve una cadena de caracteres como salida. El objetivo del ejercicio
# es apoyarnos en esta función para obtener una lista de elementos al final del
# programa.

print("Por favor añada todos los números enteros que desee hasta que no")
print("quieras añadir más, en ese caso insere 'q'")
L1 = list()
l = ''
while l != 'q':
    l = input("añadir: ")
    L1.append(l)

print(L1)