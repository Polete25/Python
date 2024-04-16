# Escribe un programa que acepte un operador matemático (+,-,* o /) y dos 
# números. Luego, el programa debe caluclar el resultado basado en dicho 
# operador.

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))
operador = input("introduce un operador: ")

if operador == '+':
    res = numero1 + numero2
    print(f"Resultado: {res}")    
elif operador == '-':
    res = numero1 - numero2
    print(f"Resultado: {res}")
elif operador == '/':
    res = numero1 / numero2
    print(f"Resultado: {res}")
elif operador == '*':
    res = numero1 * numero2
    print(f"Resultado: {res}")
else:
    print("Operador invalido.")