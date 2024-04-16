# Escribir una función numOcFichero(rutaFichero,palabra) que tome como parámetro
# la ruta del fichero rutaFichero y una palabra. La función debe devolver el 
# número de veces que la palabra aparece en el fichero pasado como parámetro.
# Nota: Suponemos que las palabras están separadas por espacios. 

def numOcFichero(rutaFichero,palabra):
    
    fichero = open(rutaFichero,"r")
    contenido = fichero.read()
    palabras = contenido.split(" ")
    oc_pala = 0
    for p in palabras:
        if p == palabra:
            oc_pala += 1
    
    return oc_pala

numOcFichero("ruta","palabra")
            