# Escribir un programa que permita recuperar la extensión de un archivo

import os

ruta_archivo = r'C:/Users/polalomarcasa/Documents/GIT_Repos/Python Ex.'
nombre_archivo = os.path.basename(ruta_archivo)

extension_archivo = nombre_archivo.split(".")[-1]

print("Extensión archivo: ", extension_archivo)