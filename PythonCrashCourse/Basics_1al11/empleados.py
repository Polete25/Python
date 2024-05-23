
class Empleados():
    def __init__(self, nombre, apellido, salario = 25000):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def dar_aument(self, aumento=5000):
        self.salario = self.salario + aumento
        


        