# Crea una clase Persona con:
# atributos: nombre, edad
# un método saludar() que devuelva: "Hola, me llamo {nombre} y tengo {edad} años."

class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        saludar = f'Hola, me llamo {self.nombre} y tengo {self.edad} años.' 
        return saludar

p1 = Persona("Pol",31)

print(p1.saludar())