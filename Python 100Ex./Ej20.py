# Escribir un programa que muestre en la consola el valor de las claves
# 'Manzana' y 'Banana' del diccionario {'Manzana':3,'Banana':7,'Kiwi':1}

d = {'Manzana':3,'Banana':7,'Kiwi':1}

for key in d.keys():
    if key != 'Kiwi':
        print(key)
