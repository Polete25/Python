# Escribir una función sumaMayor(L) que toma como parámetro una lista L y 
# determina la suma más grande obtenida al sumar los elementos de todas las 
# subsecuencias posibles de la lista L. La función debe devovler la subsecuencia 
# que devuelve la suma más grande y la suma máxima encontrada. Recordatorio: una
# substancia es una secuencia de números en la lista L.

def sumasec(L,i,j):
    Lij = L[i:j+i]
    return(Lij)

def sumaMayor(L):
    suma_max = L[0]
    for i in range(len(L))    :
        for j in range(i,len(L)):
            s = sumasec(L,i,j)
            if s > suma_max:
                secuencia = L[i:j+1]
                suma_max = s
                
    return suma_max,secuencia

