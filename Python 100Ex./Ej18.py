# Escriba un programa que permita ordenar una lista de tuplas L en orden 
# ascendente, basándose en el segundo elemento de la tupla. La lista que
# consideramos en este ejercicio es:

L = [("Manzana",15),("Banana",8),("Fresa",12),("Kiwi",9),("Melocoton",2)]

L.sort(key = lambda x : x[1], reverse=False)
print(L)
