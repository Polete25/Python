# Escribir una función llamada presenciaVocal(frase) que tome como parámetro una 
# frase y verifique si contiene una vocal o no. Si la frase contiene una vocal,
# la función devuelve True, de lo contrario devuelve False.

def presenciaVocal(frase):
    vocales = ('a','e','i','o','u')
    for f in frase:
        if f in vocales:
            return True
    return False

print(presenciaVocal("Voy a darme una ducha"))
print(presenciaVocal("rbhpm"))
