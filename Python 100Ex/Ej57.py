# Escribir una función invertirFrase(frase) que toma una frase como parámetro y
# invierte el orden de las palabras en la frase. La función debe devolver la 
# frase con las palabras invertidas. Nota: se considera que las palabras en una 
# frase están separadas por espacios. 

def invertirFrase(frase):
    palabras = frase.split(" ")
    palabras.reverse()
    frase = " ".join(palabras)
    return frase

print(invertirFrase("hola a todo el mundo"))
