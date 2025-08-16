# Escribir un programa que permita sumar los valores del siguiente diccionario:

d = {"Manzanas":15,"Banana":8,"Fresas":12,"Kiwi":9,"Melocotón":2}

# Mi solución @polalomar25:
tot = 0
for value in d.values():
    tot += value
print(tot)

#Solución:
print(sum(d.values()))
