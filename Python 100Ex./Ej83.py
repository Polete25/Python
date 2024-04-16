# Escribir una función esDistinto(numero) que toma como parámetro un número 
# entero y verifica si todos los dígitos de este número son diferentes. La 
# función debe devolver True si el número contiene dígitos todos distintos y 
# False en caso contrario.

def esDistinto(numero):
    numero = str(numero)
    L1 = list(numero)
    for n in L1:
        str(n)
        L1.remove(n)
        if n in L1:
            return False
    return True

print(esDistinto(9647))
print(esDistinto(1343))

# not working, don't know why

# or 

def esDistinto(numero):
    numero_str = str(numero)
    for digito in numero_str:
        if numero_str.count(digito) >= 2:
            return False
    return True

print(esDistinto(9647))
print(esDistinto(1343))


