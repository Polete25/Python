# Crea una clase base Vehiculo con atributos marca, modelo y un método descripcion().
# Luego crea dos subclases:
# Coche con atributo extra puertas
# Moto con atributo extra cilindrada

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f'{self.marca} {self.modelo}'

class Coche(Vehiculo):
    def __init__(self, puertas, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.puertas = puertas
    
class Moto(Vehiculo):
    def __init__(self, cilindrada, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

    def motaka(self):
        return f'{self.marca} {self.modelo} {self.cilindrada}'

motoPol = Moto(490,'KTM','Adventure')

print(motoPol.motaka())



