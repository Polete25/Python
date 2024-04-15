# Escribir una función tratamientoFichero(rutaFichero) que tome como parámetro 
# un fichero de texto y cree otro fichero de texto sgún la ruta que elijas) que
# contendrá el mismo contenido del fichero pasado como parámetro pero sin saltos 
# de línea.

def tratamientoFichero(rutaFichero):
    with open(rutaFichero, "r") as fichero1:
        with open('Prueba_2.txt',"w") as fichero2:
            for linea in fichero1:
                fichero2.write(linea.rstrip("\n"))
                
