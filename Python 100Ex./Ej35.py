# Escribe una función llamara VeriPresencia(a,L) que toma como parámetro una 
# list L y un elemento a. La función devuelve True si el elemento existe en la 
# lista L y False si el elemento a no existe en la lista L.

def VeriPresencia(a,L):
    i = 0
    for l in L:
        if l == a:
            i += 1
    if i == 1:
        return True
    else: 
        return False
    

print(VeriPresencia(2,[1,2,3,4,5,6]))
print(VeriPresencia(-1,[3,6,9,7,"abcr"]))

# or 

def VeriPresencia(a,L):
    
    if a in L:
        return True
    else:
        return False

