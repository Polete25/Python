# Escribir una clase de Python llamada "Persona" que tendrá tres atributos que 
# definen ciertar caracteristicas de una persona real: altura (m), peso (kg) y
# edad. Esta clase Python tendrá dos métodos: CalculoMC(self) que determina el
# índice de masa corporal (IMC) de la persona. - InterpretacionIMC(self) que 
# muestra "El resultado del cálculo del IMC indica que la persona tiene bajo 
# peso (delgadez)" si el resultado devuelto por calculoIMC(self) es menor o 
# igual a 18,5. Si el resultado es mayor o igual a 30, muestra "La persona es 
# obesa". De lo contrario, muestra "La persona tiene sobrepeso o una complexión 
# normal". Recordatorio: El índice de masa corporal (IMC) se calucla mediante la
# fórmula peso / (altura**2)

class persona():
    
    def __init__(self, altura, peso, edad):
        self.atura = altura
        self.peso = peso
        self.edad = edad
        
    def imc(self):
        imc = self.peso / self.atura**2
        return imc
    
    def result(self):
        if self.imc() <= 18.5:
            print("La persona es obesa")
        else:
            print("La persona tiene sobrepeso o una complexión normal")
            
julian = persona(1.91,90,26)
julian.imc()
julian.result()

    
    