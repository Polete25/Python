# Escribir una función recursiva secuenciaFibonacci(N) que tome como parámetro 
# un número natural N positivo y devuelva el elemento de índice N de la sucesión 
# de Fibonacci. Recordatorio: estamos interesados en la sucesión de enteros 
# definida por F1 = 1, F2 = 1 y para cualquier número natural N, por 
# F(N+2) = F(N+1) + F(N). 



def fibo(x):
    x = int(x)
    
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    list = [0,1]
    c = 2
    while c <= x:
        fib = list[c-1] + list[c-2]
        list.append(fib)
        c += 1
    
    return(fib)

print(fibo(25))
print(fibo(45))


# or (solución del libro.. está mal)

"""

def secuenciaFibonacci(N):
    if N <= 2:
        return 1
    
    return secuenciaFibonacci(N-1) + secuenciaFibonacci(N-2)

secuenciaFibonacci(45

"""