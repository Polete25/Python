# Escriba una clase Cadena Perso que sea una cadena de caracteres personalizada. 
# Nuestra cadena de caracteres personalizada no debe contener números ni comas 
# ni puntos. En este ejercicio, deberá crear los métodso que nos permitirán 
# realizar las siguientes operaciones: 
# >> cadena1 = cadenaPerso("Ho,la")
# La instancia creada solo debe contener letras alfabéticas.
# El caracter ',' será eliminado.
# >> cadena1 + ","
# No se puede agregar una ',' a la cadena.
# cadena1 + "."
# No se puede agregar un '.' a la cadena
# >> cadena2 = cadena1 + "¿Cómo estás?"
# >> cadena2
# 'Hola ¿cómo estás?'

import string
lista_caracteres = list(string.digits) + [",","."]
class CadenaPerso:
    def __init__(self,cadena):
        self.cadena = cadena
        lista_cadena = list(cadena)
        for c in lista_cadena:
            if c in lista_caracteres:
                print("La instancia creada debe contener sólo letras alfabéticas")
                print(f"el caracter '{c}' será eliniado")
        self.cadena = cadena
    
    def __add__(self,nueva_cadena):
        if nueva_cadena in lista_caracteres:
            return f"No se puede agregar un '{nueva_cadena}' a la cadena"
        else: 
            self.cadena += nueva_cadena
        return self.cadena
    
    def __repr__(self):
        return self.cadena
    
cadena1 = CadenaPerso("Ho,la")
print(cadena1 + ",")
print(cadena1 + ".")
cadena2 = cadena1 + "¿como estas?"
cadena2
        
                
                
    