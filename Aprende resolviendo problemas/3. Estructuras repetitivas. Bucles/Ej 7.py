# Escribe un programa que busque números primos del 1 al N según la entrada del
# usuario.

num = int(input("Introduce un número: "))

for num in range(1, num + 1):
    isPrime = True
    
    if num == 1 or num == 0:
        isPrime = False
    for x in range(2,num):
        if num % x == 0:
            isPrime = False
    if isPrime:
        print(num, end=" ")