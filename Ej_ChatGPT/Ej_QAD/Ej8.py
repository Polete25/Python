# Escribir funciones que encuentren el máximo y el mínimo de una lista sin usar max() ni min().

def max_min(lista: list):
    max = lista[0]
    min = lista[0]
    for l in lista:
        if max < l:
            max = l
        if min > l:
            min = l
    return max, min

print(max_min([1,3,4,5,6,7,8]))