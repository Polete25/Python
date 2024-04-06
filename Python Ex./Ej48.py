# Escribe una función concatListas(L1,L2,L3) que tome tres listas L1,L2 y L3 
# como parámetro y devuelva la concatenación de estas tres listas.

def concatListas(L1,L2,L3):
    L4 = list()
    for l in L1:
        L4.append(l)
    for l in L2:
        L4.append(l)
    for l in L3:
        L4.append(l)
    return L4  
        
print(concatListas([0,9,8],[True,False,"abc"],[0,9,8,2,6,9,True,False,"abc"]))
print(concatListas([[38,-1],3,-9],["xz","Francia"],[]))

# or 

def concatListas(L1,L2,L3):
    L_concat = L1 + L2 + L3
    return L_concat

print(concatListas([0,9,8],[True,False,"abc"],[0,9,8,2,6,9,True,False,"abc"]))
print(concatListas([[38,-1],3,-9],["xz","Francia"],[]))


