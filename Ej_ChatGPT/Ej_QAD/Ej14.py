# Dada una lista de números enteros, escribe una función que:
# Elimine los elementos duplicados,
# Devuelva la lista ordenada de menor a mayor sin usar sorted() ni sort().

def limp_list(lista: list) -> list:
    no_dupl = []
    for l in lista:
        if l not in no_dupl:
            no_dupl.append(l)
    
    n = len(no_dupl)
    for i in range(n):
        for j in range(0, n-i-1):
            if no_dupl[j] > no_dupl[j+1]:
                no_dupl[j], no_dupl[j+1] = no_dupl[j+1], no_dupl[j]

    return no_dupl

print(limp_list([4, 2, 7, 6, 2, 1, 4]))