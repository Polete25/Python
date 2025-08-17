# Generar la secuencia de Fibonacci hasta un número n.

def fibonaccifor(n: int) -> list:
    fibo = [0,1]

    for i in range(0, n+1):
        if fibo[-1]+fibo[-2] <= n:
            fibo.append(fibo[-1]+fibo[-2])
        else:
            break
    
    print(fibo)


fibonaccifor(99)

def fibonacciWhile(n: int) -> list:
    fibo = [0,1]

    while fibo[-1]+fibo[-2] < n:
        fibo.append(fibo[-1]+fibo[-2])

    
    print(fibo)


fibonacciWhile(99)

