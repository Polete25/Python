#Imprimir los números del 1 al 50, pero:
  # Si es múltiplo de 3 → imprimir "Fizz"
  # Si es múltiplo de 5 → imprimir "Buzz"
  # Si es múltiplo de ambos → imprimir "FizzBuzz"

def fizzbuzz(n):
    for num in range(1,n+1):
        if num%3 == 0 and num%5 == 0:
            print("FizzBuzz")
        elif num%3 == 0:
            print("FIZZ")
        elif num%5 == 0:
            print("BUZZ")
        else:
            print(num)

fizzbuzz(100)

