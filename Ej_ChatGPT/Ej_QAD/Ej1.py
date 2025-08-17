# Escribir una función que verifique si una palabra
# o frase es un palíndromo (se lee igual al derecho 
# y al revés, ignorando espacios y mayúsculas).

def palindromo(palabra: str):
    palabra = palabra.lower().replace(" ","")
    return palabra == palabra[::-1]

print(palindromo("Hola"))
