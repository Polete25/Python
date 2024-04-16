# Escribe una función leerFichero(rutaFichero) que toma como parámetro la ruta 
# completa del fichero rutaFichero y devuvelve su contenido. El contenido del 
# fichero debe mostrarse en la consola. Nota: para este ejercicio, tendría que 
# crear un fichero de texto con contenido para probar su función. 

def leerFichero(rutaFichero):
    fichero = open(rutaFichero,"r")
    contenido = fichero.read()
    fichero.close()
    return contenido

leerFichero(r"rutaFichero")