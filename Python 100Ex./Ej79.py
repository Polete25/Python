# Escribir una función isdigit(cadena) que permita verificar sila cadena es un 
# número o no. La función devuelve True si la cedena es un número y false si no
# lo es. 

def isdigit(cadena):
    L1 = list(cadena)
    L2 = ['0','1','2','3','4','5','6','7','8','9']
    for l in L1:
        if l not in L2:
            return False
    return True
            
print(isdigit("125920"))
print(isdigit("edgte9eb"))
