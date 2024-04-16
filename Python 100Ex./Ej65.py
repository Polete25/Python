# Escribir una función nombreFichero(rutaDirectorio) que toma como parámetro la
# ruta del directorio rutaDirectorio y devuelve el número de ficheros contenidos 
# en el directorio pasado como parámetro.


import os

def nombreFichero(rutaDirectorio):
    num_fichero = 0
    listar_contenido = os.listdir(rutaDirectorio)
    for contenido in listar_contenido:
        if os.path.isfile(os.path.join(rutaDirectorio,contenido)):
          num_fichero += 1
        
    return num_fichero  

help(os.path.join)