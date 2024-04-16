# Escribir una función llamada divisoresMult(n,a,numUmbral) que permita 
# encontrar los números (desde 0 hasta un numUmbral dado) que son divisibles por
# n y que no son múltiplos de a.

def divisoresMult(n,a,numUmbral):
    L1 = list()
    for u in range(numUmbral+1):
        if u % n == 0 and u % a != 0:
            L1.append(u)
    return L1

print(divisoresMult(5,2,100))
print(divisoresMult(11,3,85))