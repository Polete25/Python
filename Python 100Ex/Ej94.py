# Escribr unaclase punto2D que representa un punto en un espacio 2D. Nuestra 
# clase debe contener dos atributos x e y. En este ejercicio, queremos realizar 
# algunas operaciones con las instancias que crearemos a partir de la clase 
# Punto2D, utilizando operadores estándar como +.-,* etc. Para hacer esto, aquí
# está la lista de métodso especiales a crear para esta función: 
#       __add__(self,p) que nos permitirá realiszar la operación p1-p2
#       __sub__(self,p) que nos permitirá realizar la operación p1-p2
#       __mul__(self,p) que nos permitirá realizar la operación p1*p2
#       __truediv__(self,p) que nos permitirá realizar la operación p1/p2
# Recordatorio: La sobrecarga de operadores consiste en crear métodos especiales 
# en la clase que nos permitan ulizar los operadores estándar como +,-,*,/ y así
# sucesivamente.

class punto2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,p):
        return self.x + p.x, self.y + p.y

    def __sub__(self,p):
        return self.x - p.x, self.y - p.y
    
    def __mul__(self,p):
        return self.x * p.x, self.y * p.y
    
    def __truediv__(self,p):
        return self.x / p.x, self.y / p.y

p1 = punto2D(3,2)
p2 = punto2D(1,4)

print("p1-p2: ",p1-p2)
print("p1*p2: ",p1*p2)
print("p1/p2: ",p1/p2)
