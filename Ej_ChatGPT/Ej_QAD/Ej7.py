# Contar cuántas veces aparece cada letra en una cadena (similar a collections.Counter pero hecho a mano).

def contar_letra(texto: str) -> dict:
    dictio = {}
    for letra1 in texto:
        count = 0
        for letra2 in texto:
            if letra1.upper() == letra2.upper():
                count = count+1
        
        dictio.update({letra1:count})

    return dictio

print(contar_letra('Hola Que tal, como estas?'))
