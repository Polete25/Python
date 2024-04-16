# Escriba un programa que, dadas dos listas L1 y L2, devuelva una lista L3 que 
# contenga los elemetos en común entre L1 y L2.
# Para probar, vamos a tomar las listas:

L1 = [9,8,7,14,3,2,"a","p","hola","b"]
L2 = ["b",1,9.2,6,3,9,"p"]

# Metodo de @PolAlomar25
L3 = []
for l1 in L1:
    for l2 in L2:
        if l1 == l2:
            L3.append(l1)
print(L3)

#Solución
L3 = set(L2).intersection(set(L1))
L3 = list(L3)
print(L3)