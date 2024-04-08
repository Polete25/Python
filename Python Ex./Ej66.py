# Escribir una función escribirFichero(rutaFichero,texto) que tome como parámetro
# el nombre del archivo nomFichero y el texto que queremos escribir en el 
# fichero. La función nos permitirá al final tener un archivo que contega el 
# texto pasado como parámetro. Nota: Suponemos en este ejercicio que el fichero 
# de texto está vacío al principio.

def escribirFichero(rutaFichero,texto):
    f = open(rutaFichero,"w")
    f.write(texto)
    f.close

mirutafichero = r"ruta"
miTexto = "Hola, me llamo Gregory y tengo 30 años"

escribirFichero(mirutafichero,miTexto)