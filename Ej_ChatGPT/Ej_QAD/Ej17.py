# Crea una clase CuentaBancaria con:
# atributos: titular, saldo (inicia en 0)
# métodos:
# depositar(monto) → aumenta el saldo
# retirar(monto) → disminuye el saldo si hay suficiente dinero
# mostrar_saldo() → imprime el saldo actual


class CuentaBancaria():
    def __init__(self, titular, saldo: int = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,monto):
        self.saldo += monto
    
    def retirar(self,monto):
        self.saldo -= monto
    
    def mostrar_saldo(self):
        print(f'{self.titular}, tu saldo es de: {self.saldo}')


cuenta1 = CuentaBancaria('Pol')

cuenta1.mostrar_saldo()
cuenta1.depositar(100)
cuenta1.mostrar_saldo()
cuenta1.retirar(50)
cuenta1.mostrar_saldo()







