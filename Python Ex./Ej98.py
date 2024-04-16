# Escrbir una función ordenarDicc(d) que toma como parámetro un diccionario d
# y devuelve un diccionario ordenado en orden ascendente según las claves del 
# diccionario. Instruccion: Las claves del diccionario d no deben contener una 
# mezcla de cadenas de caracteres y números.

def ordenDicc(d):
    lista_tuplas = []
    claves_d = list(d.keys())
    valores_d = list(d.values())
    
    for clave,valor in zip(claves_d,valores_d):
        lista_tuplas.append((clave,valor))
        
    lista_tuplas.sort(key = lambda x : x[0])
    
    return dict(lista_tuplas)