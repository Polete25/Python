# Escribir una función llamada anadirElementoDicc(clave,valor,d) que toma 3 
# parámetros de entrada: un diccionario d, una clave y su valor asociado d. Por 
# último, la función debe devolver el diccionario d que contiene la nueva clave.

def anadirElementoDicc(clave,valor,d):
    d[clave] = valor
    return d

print(anadirElementoDicc('Baptiste',29,{'Julien':14,'Laurent':31}))
print(anadirElementoDicc('Peso',65.3,{}))
