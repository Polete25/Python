# Escribir una función join(L,caracter) que permita transformar una lista L en 
# una cadena de caracteres con el separador caracter pasado como parámetro.

def join(L,caracter):
    cadena_carc = ""
    for i in range(len(L)):
        cadena_carc += L[i]
        if i != len(L)-1:
            cadena_carc += caracter
    return cadena_carc

print(join(["Hola","Aurélia"]," "))
print(join(["Hola","¿Está bien?"],". "))


    