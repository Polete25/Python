# Escribir una función calculoMCD(a,b) que tome como parámetro dos enteros a y b 
# y calcule el máximo común divisor utilizando el algoritmo de Euclides.

def calculoMCD(a,b):
    if b > a:
        a,b = b,a
    
    c = a
    r = b
    
    while r != 0:
        temp = r
        r = c % r
        c = temp
    
    return c

print(calculoMCD(5,3))
print(calculoMCD(5,15))

# or 

def calculoMCD(a,b):
    assert(a>0 and b>0)
    while b!=0:
        a,b = b,a%b
        
    return a

print(calculoMCD(5,3))
print(calculoMCD(5,15))