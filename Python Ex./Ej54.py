# Escribir una función llamada EliminarEsp(frase) que tome como parámetro una 
# frase en forma de cadena de caracteres y devuelve esa misma frase sin los 
# espacios (si los hay) entre las palabras.

def eliminarEsp(frase):
    return frase.replace(" ","")
    

print(eliminarEsp("Hola que tal"))