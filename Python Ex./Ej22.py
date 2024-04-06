# Escribir un programa que permita truncar un número decimal a 2 cifras después 
# de la coma. Por ejemplo, si tomamos el numero decimal 187,632587, el programa
# deberá mostar 187,63

n = 187.632587

# Mi solución @polalomar25:
n = round(n,2)
print(n)

#Solución:
print(float("{:.2f}".format(187.632587)))