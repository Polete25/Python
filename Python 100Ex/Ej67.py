# Escribir una función claveMaxValDicc(d) que tome como parámetro un diccionario
# d y devuelva la clave que tiene el mayor número de valores únicos. Nota: En 
# este ejercicio, consideramos que los valores de todas las claves están en 
# forma de listas.

def claveMaxValDicc(d):
    max = ''
    max_uni = 0
    for K1,L1 in d.items():
        unic = 0
        for l in L1:
            if L1.count(l) == 1:
                unic += 1
        if unic > max_uni:
            max = K1
            max_uni = unic
            
    return max
               
               
print(claveMaxValDicc({"a":[9,10,9,7,3,1],
                       "b":[5,3,2,2,2],
                       "c":[1,1,1,1,1,1,8,2]})) 
    
    
