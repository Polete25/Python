# Escribir una función reemplazar(frase, palabra, nuevaPalabra) que permita 
# reemplazar en la cadena de caracteres frase, la palabra introducida en el 
# segundo parámetro por la palabra nuevaPalabra. La función debe devolver la 
# frase con nuevaPalabra reemplazando la palabra ya existente en la frase.

def reemplazar(frase, palabra, nuevaPalabra):
    frase = frase.replace(palabra,nuevaPalabra)
    return frase

print(reemplazar("Hola Aurélia","Aurélia","Mathilde"))

# or 

def reemplazar(frase, palabra, nuevaPalabra):
    if palabra in frase:
        inicio_palabra_idx = frase.index(palabra)
        fin_palabra_idx = inicio_palabra_idx + len(palabra)
        frase_lista = list(frase)
        frase_lista[inicio_palabra_idx:fin_palabra_idx] = nuevaPalabra
        frase = "".join(frase_lista)
    
    return frase

print(reemplazar("Hola Aurélia","Aurélia","Mathilde"))
