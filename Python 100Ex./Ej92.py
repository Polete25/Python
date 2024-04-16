# Escribir una clase CuentaBancaria que nos permita gestionar una cuenta 
# bancaria. Esta clase tendrá dos atributos: nombre y saldo. Por defecto, los
# atributos tienen los siguientes valores: nombre = "Maxime", saldo = 600.
# Eta clase debe contener los siguientes 3 métodos: 
#   - deposito(self,cantidad) que permitirá agregar una cierta cantidad al saldo
#   - retiro(self,cantidad) que permitirá mostrar el nombre del tirular y el 
#       saldo de su cuenta.

class cuentaBancaria:
    def __init__(self,nombre = "Maxime", saldo = 600):
        self.nombre = nombre
        self.saldo = saldo
        
    def deposito(self,cantidad):
        self.cantidad = cantidad
        self.saldo += cantidad
        return self.saldo
    
    def retiro(self,cantidad):
        self.cantidad = cantidad
        self.saldo -= cantidad
        return self.saldo
    
    def __repr__(self):
        return "El saldo de la cuenta bancaria de "+self.nombre+" es de "+ str(self.saldo) + "€."
    

cuenta1 = cuentaBancaria("Julie",1000)
cuenta1.deposito(400)
cuenta1.retiro(100)
print(cuenta1)
    
cuenta2 = cuentaBancaria()
cuenta2.deposito(500)
print(cuenta2)
        
    