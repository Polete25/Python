# Escribir un programa que muestre la carpeta en la que se encuentra el script
# Python actual.

import os

# Obtener la ruta absoluta del directorio actual donde se ejecuta el script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Imprimir la ruta del directorio actual
print("El directorio actual del script es:", current_directory)

# Solución:

import os

print(os.getcwd())