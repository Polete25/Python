# Escribir una función presenciaNumero(rutaFichero) que toma como parámetro la 
# ruta del fichero rutaFichero y verifica si el fichero contiene un número. La
# función devuelve True si el fichero contien un número y False en caso 
# contrario.

def presenciaNumero(rutaFichero):
    fichero = open(rutaFichero,"r")
    contenido = fichero.read()
    for c in contenido:
        if c.isdigit():
            return True
        
    return False


