# Escriba una función numValoresDicc(d) que tome un diccionario d como parámetro
# y devuelva el número de valores contenidos en las listas asociadas a las 
# claves. Nota: A efectos de este ejercicio, consideramos que todos los valores
# asociados a las claves están en forma de listas

def numValoresDicc(d):
    i = 0
    for valor in d.values():
        for v in valor:
            i += 1
    return i

print(numValoresDicc({"a":[1,2,3],"b":[3,"p"],"c":[8]}))
print(numValoresDicc({"Julie":[12,60.1],"Fred":[26,75.6],"David":[]}))