# Escribir una clase NumeroComplejo que represente los números complejos (en el 
# sentido matemático del término). Esta clase tendrá dos atributos: real e img
# Recordatorio: un número complejo consta de una parte real y una parte 
# imaginaria. Este nñumero se escribe en forma de 5+3i, donde el número 5 
# representa la parte real y el número 3 representa la parte imaginaria.
# En este ejercicio, queremos tener los siguientes resultados, al llamar a una 
# instancia de la clase o hacer un print() de esta instancia:
# num1 = NumeroComplejo(2,7) >> num1 >> 2+7i >> print(num1) >> 2+7i
# Para ello, habría que crear los sigueintes métodos especiales:
# __str__(self) que nos permitirá tener la buena visualización con la ayuda 
# print(). / __repr__(self) que nos permitirá tener la buena visualización al 
# llamar a una instancia. 

class numerocomplejo:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def __str__(self):
        return f"({self.real} + {self.img}i)"
        
    def __rept__(self):
        return str(self.real) + " + " + str(self.img) + "i"
    
num1 = numerocomplejo(2,6)

print(num1)

num1