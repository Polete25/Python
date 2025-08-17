# Escribe una función que reciba una cadena de texto y devuelva True
#  si es un palíndromo (se lee igual de izquierda a derecha que de
#  derecha a izquierda, ignorando espacios y mayúsculas).

def palin(texto: str) -> bool:
    texto = texto.upper().replace(" ","")
    return texto == texto[::-1] 

print(palin("Anita lava la tina"))    
    