# Escribir una clase Paralelepípedo que herede de la clase rectángulo del 
# ejercicio anterior. La clase paralelepípedo debe contener, además de los 
# atributos heredados, el atributo altura (cm).

class rectangulo:
    def __init__(self,ancho,largo):
        self.ancho = ancho
        self.largo = largo
        
    def perimetro(self):
        return self.ancho*2 + self.largo*2
    
    def superficie(self):
        return self.ancho * self.largo

class paralelepipedo(rectangulo):
    def __init__(self,ancho,largo,alto):
        super().__init__(ancho,largo)
        self.alto = alto
    
    def volumen(self):
        return self.ancho * self.largo * self.alto 
    
paralelepipedo1 = paralelepipedo(9,5,2)
print(paralelepipedo1.perimetro())
print(paralelepipedo1.volumen())