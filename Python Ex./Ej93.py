# Escribir una clase coche que nos permita gestionar los coches de alquiler. La
# clase trendrá 4 atributos que representan varias características: marca, color
# nombreConductor y kmInicio. Por defecto, estos atributos tienen los siguientes
# valores. marca = 'peugot', color= 'negro', nombreConductor = 'ninguno', 
# kmInicio = 16900. Esta clase debe contener los siguientes 3 métodos:
#       - seleccionConductor(self,nombreConductor) que permitirá designar o 
#           cambiar el nombre del conductor del coche.
#       - distanciaRecorrida(self,kmFin) que permitirá calcular la distancia
#           recorrida por el conductor durante el periodo de alquiler.
#       - mostrarInfo(self,kmActual) que nos permitirá mostrar el estado actual
#           del coche, es decir, el nombre del conductor, la marca, el color y 
#           el kilometraje actual.


class coche:
    def __init__(self, marca = 'peugot', color = 'negro', nombreConductor \
        = 'Ninguno', kmInicio = 16900):
        self.marca = marca
        self.color = color
        self.nombreConductor = nombreConductor
        self.kmInicio = kmInicio
    
    def seleccionConductor(self,nombreConductor1):
        self.nombreConductor = nombreConductor1
        return self.nombreConductor
    
    def distanciaRecorrida(self,kmFin):
        self.kmFin = kmFin
        distancia_reco = kmFin - self.kmInicio
        return distancia_reco
    
    def mostrarInfo(self,kmActual):
        self.kmActual = kmActual
        return "El coche "+ str(self.marca) + " de color "+ str(self.color) +\
            " cuyo conductor es "+ str(self.nombreConductor) +\
                ", tiene un kilometraje actual de "+ str(self.kmActual) +"km."
        
coche1 = coche()
print(coche1.seleccionConductor("Patrick"))
print(coche1.distanciaRecorrida(20000))
print(coche1.mostrarInfo(20000))

