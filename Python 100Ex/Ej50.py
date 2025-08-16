# Escribe una función concatDicc(d1,d2) que tome dos diccionarios d1 y d2 como 
# parámetros y devuelva la concatenación de estos los diccionarios 21 y d2

def concatDicc(d1,d2):
    d3 = {**d1, **d2}
    return d3

print(concatDicc({"a":3,"b":6},{"c":2,"d":1}))