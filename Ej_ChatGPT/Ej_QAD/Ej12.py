# Rotar una lista k posiciones hacia la derecha.

def rotar(lista: list, k: int) -> list:
    rot_list = []
    for n in range(k, len(lista)):
        rot_list.append(lista[n])
    for n in range(0,k):
        rot_list.append(lista[n])

    return rot_list

print(rotar([1,2,4,5,67,'q'],3))