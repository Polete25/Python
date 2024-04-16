# Escribir una función llamada filtrarPalabras(frase,longitudMinimia) que tome
# como parámetro una frase y filtre las palabras con una longitud estrictamente 
# menor que el parámetro longitudMinima. La función debe devolver la misma frase 
# sin las palabras filtradas.

def filtrarPalabras(frase, longitudMinima):
    palabras = frase.split()
    for p in palabras:
        if len(p) < longitudMinima:
            frase = frase.replace(" "+p,"")
    return frase

print(filtrarPalabras("Hola a todos",4))
