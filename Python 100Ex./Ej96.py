# Escribir una clase ListaPerso que sea una lista personalizada. Nuestra lista 
# personalizada solo debe contener números y no cadenas de caracteres ni 
# booleanos. Por lo tanto, no es posible tener duplicados en nuestra lista.
# En este ejercicio, tendremos que crear los métodos que nos permitan realizar 
# las siguientes operaciones:

class ListaPerso:
    def __init__(self,*numeros):
        self.numeros = []
        for numero in numeros:
            if type(numero) == int or type(numero) == float:
                self.numeros.append(numero)
            else:
                print(f"Operación prohibida: no es posible inicializar la "/
                      "lista con {numero}")
    
    def append(self,numero):
        if type(numero) == int or type(numero) == float:
            if numero not in self.numeros:
                self.numeros.append(numero)
            else:
                return f"El número {numero} ya existe en la lista {self}"
        else:
            return f"Operación prohibida: no es posbile agregar el tipo {type(numero)}"
    
    def __repr__(self): 
        return f"{self.numeros}"
    
    def __str__(self):
        return f"{self.numeros}"    

L1 = ListaPerso(5,2,3,7,8)
print(L1)
L1.append(2)
print(L1.append("abc"))
L1.append(10)
print(L1)
        
