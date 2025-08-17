# Escribir una función que devuelva todos los números primos hasta un número dado.

def primos(n: int):
    
    primos = [1]

    for num in range(2,n+1):
        es_primo = True
        for i in range(2,int(num**0.5)+1):
            print(f'num: {num} i: {i}')
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    
    return primos

print(primos(30))