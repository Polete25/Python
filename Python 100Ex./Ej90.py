# Escribir una clase Rectangulo que tenga dos atributos: ancho (cm) y largo (cm)
# La clase Rectangulo debe contener los siguientes métodos: Perimetro(self)
# Superficie(self) 

class rectangulo:
    def __init__(self,ancho,largo):
        self.ancho = ancho
        self.largo = largo
        
    def perimetro(self):
        return self.ancho*2 + self.largo*2
    
    def superficie(self):
        return self.ancho * self.largo
    
rectangulo1 = rectangulo(10,15)
print(rectangulo1.largo)
print(rectangulo1.perimetro())
print(rectangulo1.superficie())