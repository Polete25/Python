# Quitar los repetidos pero manteniendo el orden.

def no_dupli(lista: list) -> list:
    nodupli = []
    for l in lista:
        if l not in nodupli:
            nodupli.append(l)

    return nodupli

print(no_dupli([2,3,5,73,6,2,6,4,1,4,2]))