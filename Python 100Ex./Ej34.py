# Escribe una función llamada f(a,b,x) tomando como parámetro 3 enteros a,b,x y
# devuelve e resultado la siguiente función:
#   f(a,b,x) = a * (x ** 3) + 2 * a * (x ** 2) + b

def funcion(a,b,x):
    result = a * (x ** 3) + 2 * a * (x ** 2) + b
    return result

print(funcion(3,0,1))
print(funcion(0,2,2))