# Un número n es par si n-1 es impar, y viceversa, si un número n es impar, 
# entonces n-1 es par. Escribir dos funciones recursivas mutuas, numeroPar(n)
# y numeroImpar(n), que permitan saber si un número n es par o impar.

def numeroPar(N):
    if N == 1:
        return False
    return numeroImpar(N-1)

def numeroImpar(N):
    if N == 1:
        return True
    return numeroPar(N-1)

print(numeroPar(7))
    