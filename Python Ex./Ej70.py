# Escribe una función generarContrasna(caraceteres,longitud) que tome como 
# parámetro una lista de caracteres y la longitud de la contraseña longitud, y
# luego genere aleatoriamente una constraseña con la longitud y caracteres 
# pasados como parámetros. La función debe devovler la contraseña en forma de
# una cadena de caracteres.

import random
import string

list_caracteres = list(string.ascii_letters + string.digits + "!@#$%&^/*()")

def generarContraseña(caracteres, longitud):
    random.shuffle(caracteres)
    contra_list = []
    for i in range(longitud):
        carc_ale = random.choice(caracteres)
        contra_list.append(carc_ale)
    
    random.shuffle(contra_list)
    contra = "".join(contra_list)
    
    return contra

print(generarContraseña(list_caracteres,5))