# Un triplet pitagórico es un tripleta (x,y,x) de enteros tal que x < y < z y 
# x**2 + y**2 = z**2. Existe una única tripleta pitagórica tal que x+y+z = 1000.
# ¿Cuál es el valor de x*y*z?

for x in range(0,1000):
    for y in range(x+1,1000):
        for z in range(y+1,1000):
            if x**2 + y**2 == z**2:
                if x + y + z == 1000:
                    print(x*y*z)
                