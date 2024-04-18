# Escribe un programa que cuente números positivos y negativos. El programa debe 
# dejar de ejecutarse una vez que el usuario introduzca un 0.

num = 1
pos = 0
neg = 0
while num != 0:
    num = int(input("Introduzca un número: "))    
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    
print(f"Números positivos: {pos}")
print(f"Números negativos: {neg}")



    