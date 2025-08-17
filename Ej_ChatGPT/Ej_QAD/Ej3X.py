# Implementar ordenamiento por burbuja (bubble sort).

def ord_list(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list


ord_list([13,4,6,8,0,33])