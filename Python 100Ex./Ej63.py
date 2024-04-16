# Escribir una función eliminarCaracter(rutaFichero,caracter) que toma como 
# parámetro la ruta del fichero rutaFichero y un carácter. La función debe 
# eliminar el carácter pasado como parámetro del fichero correspondiente.

def eliminarCaracter(rutaFichero, caracter):
    
    with open(rutaFichero, "r") as fichero:
        contenido = fichero.read()
    
    nuevo_contenido = contenido.replace(caracter,"")
    
    with open(rutaFichero,"w") as fichero:
        fichero.write(nuevo_contenido)
        
    return


    