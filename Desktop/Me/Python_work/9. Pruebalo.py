#9-1. Restaurante: Haga una clase llamada Restaurante. El método __init__() para
#       Restaurante debería albergar dos atributos: nombre_restaurante y 
#       tipo_cocina. Cree un método llamado describir_restaurante() que imprima 
#       estos dos datos, y un método llamado abrir_restaurante() que imprima un 
#       mensaje indicando que el restaurante está abierto. Haga una instancia
#       llamada restaurante a partir de su clase. Imprima los dos atributos por
#       separado y luego llame a ambos métodos. 

print("9.1\n")

class Restaurante:
    def __init__(self,nombre_restaurante,tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} tiene un tipo de cocina {self.tipo_cocina}.")
    def abrir_restaurante(self):
        print(f"Restaurante abierto.")
 
# ​9-2. Tres restaurantes: Empiece con la clase del ejercicio 9-1. Cree tres
#       instancias diferentes a partir de ella y llame a describir_restaurante()
#       para cada instancia.

print("9.2\n")

rest1 = Restaurante("La fiore","Italiana")
rest1.describir_restaurante()
rest2 = Restaurante("Balian","Balinesa")
rest2.describir_restaurante()
rest3 = Restaurante("La concha","Argentina")
rest3.describir_restaurante()

#​9-3. Usuarios: Cree una clase llamada Usuario. Cree dos atributos llamados 
#       nombre y apellido y otros que suelanguardarse en un perfil de usuario. 
#       Cree un método llamado describir_usuario() que imprima un resumen de la
#       información delusuario. Cree otro método llamado saludar_usuario() que 
#       imprima un saludo personalizado para el usuario. Cree varias instancias 
#       que representen a distintos usuarios y llame a ambos métodos para cada
#       usuario.

print("9.3\n")

class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def describir_usuarios(self):
        print(f"{self.nombre} {self.apellido}")
    def saludar_usuario(self):
        print(f"Saludos {self.nombre}")
    
usu1 = Usuario("Pol","Alomar")
usu1.describir_usuarios()
usu1.saludar_usuario()
usu2 = Usuario("Vini","Loco")
usu2.describir_usuarios()
usu2.saludar_usuario()

#9-4. Número servido: Empiece con el programa del ejercicio 9-1. Añada un 
#       atributo llamado número_servido con un valor predeterminado de 0. Cree 
#       una instancia llamada restaurante a partir de esta clase. Imprima el 
#       número de clientes a los que ha servido el restaurante, cambie ese valor
#       y vuelva a imprimirlo. Añada un método llamado 
#       establecer_número_servido() que le permita configurar el número de
#       clientes a los que se ha servido. Llámelo con un número nuevo y vuelva a
#       imprimir el valor. Añada un método llamado incrementar_número_servido()
#       que le permita incrementar el número de clientes atendidos. Llámelo con 
#       cualquier número que pueda representar a cuántos clientes se ha servido
#       en un día laborable normal.

print("9.4\n")

class Restaurante:
    def __init__(self,nombre_restaurante,tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0
    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} tiene un tipo de cocina {self.tipo_cocina}.")
    def abrir_restaurante(self):
        print(f"Restaurante abierto.")
    def establecer_número_servido(self,numero):
        self.numero_servido = numero
        print(f"N* de personas servidas: {numero}")
    def incrementar_número_servido(self,incremento):
        self.numero_servido += incremento
        print(f"N* de personas servidas: {self.numero_servido}")

resta1 = Restaurante("Pepito","Italiana")
resta1.establecer_número_servido(34)
resta1.incrementar_número_servido(6)

#9-5. Intentos de inicio de sesión: Añada un atributo intentos_inicio a la clase
#       Usuario del ejercicio 9-3. Escriba un método llamado 
#       incrementar_intentos_inicio() que aumente el valor de intentos_inicio en
#       1. Escriba otro método llamado restablecer_intentos_inicio() que 
#       restablezca el valor de intentos_inicio a 0. Haga una instancia de la 
#       clase Usuario y llame varias veces a incrementar_intentos_inicio(). 
#       Imprima el valor de intentos_inicio para asegurarse de que se ha 
#       incrementado correctamente y luego llame a 
#       restablecer_intentos_inicio(). Vuelva a imprimir intentos_inicio para
#       asegurarse de que se ha restablecido a 0.

print("9.5\n")

class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_inicio = 0
    def describir_usuarios(self):
        print(f"{self.nombre} {self.apellido}")
    def saludar_usuario(self):
        print(f"Saludos {self.nombre}")
    def incrementar_intentos_inicio(self):
        self.intentos_inicio += 1
    def restablecer_intentos_inicio(self):
        self.intentos_inicio = 0

usua1 = Usuario("Pol","Alomar")
usua1.incrementar_intentos_inicio()
usua1.incrementar_intentos_inicio()
usua1.incrementar_intentos_inicio()
print(usua1.intentos_inicio)
usua1.restablecer_intentos_inicio()
print(usua1.intentos_inicio)

#9-6. Carrito de helados: Un carrito de helados es, en cierto modo, parecido a 
#       un restaurante. Escriba una clase llamada CarritoDeHelados que herede de
#       la clase Restaurante del ejercicio 9-1 o del 9-4. Servirá cualquiera de 
#       las dos versiones, así que coja la que más le guste. Añada un atributo
#       llamado sabores que almacene una lista de sabores de helado. Escriba un 
#       método que muestre los sabores. Cree una instancia de CarritoDeHelados y
#       llame a ese método.

print("\n9.6\n")

class CarritoDeHelado(Restaurante):
    def __init__(self,nombre_restaurante,tipo_cocina,sabores=""):
        super().__init__(nombre_restaurante,tipo_cocina)
        self.sabores = ["Vainilla","Fresa","Chocolate"]
    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")
    
choco = CarritoDeHelado("Chocos","Frio")
choco.mostrar_sabores()
            
        


#​9-7. Admin: Un administrador es un tipo especial de usuario. Escriba una clase 
#       llamada Admin que herede de la clase Usuario  del ejercicio 9-3 o del 
#       9-5. Añada un atributo privilegios que acoja una lista de cadenas como 
#       "puede añadir comentario", "puede borrar comentario", "puede vetar 
#       usuarios", etc. Escriba un método llamado show_privileges() que enumere 
#       el conjunto de privilegios del administrador. Cree una instancia de 
#       Admin y llame al método.

class Admin(Usuario):
    def __init__(self,nombre,apellido,privilegios=""):
        super().__init__(nombre,apellido)
        self.privilegios = "- Leer\n- Escribir\n- Añadir comentarios"
    def show_privileges(self):
        print(self.privilegios)
        
admin1 = Admin("Pol","Alomar")
admin1.show_privileges()

#9-8. Privilegios: Escriba una clase Privilegios aparte. Esta clase debería 
#       tener un atributo, privilegios, que almacene una lista de cadenas como 
#       la descrita en el ejercicio anterior. Mueva el método show_privileges()
#       a esta clase. Haga una instancia de Privilegios como atributo de la 
#       clase Admin. Cree una nueva instancia de Admin y use su método para 
#       mostrar los privilegios. 

class Privilegios:
    def __init__(self):
        self.privilegios = ["- Leer", "- Escribir", "- Añadir comentarios"]

    def show_privileges(self):
        print("Privilegios:")
        for privilegio in self.privilegios:
            print(privilegio)

class Admin(Usuario):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        # Instancia de Privilegios como atributo
        self.privilegios = Privilegios()

    def show_privileges(self):
        self.privilegios.show_privileges()

# Crear una nueva instancia de Admin
admin1 = Admin("Pol", "Alomar")
admin1.show_privileges()

#​9-9. Mejora de Battery: Use la última versión de electric_car.py. Añada un 
#       método a la clase Battery llamado upgrade_battery(). Este método debería
#       comprobar el tamaño de la batería y establecer la capacidad en 65 si no
#       está ya así. Haga un coche eléctrico con un tamaño de batería 
#       predeterminado, llame a get_range() una vez y vuelva a llamarlo para
#       mejorar la batería. Debería ver un incremento en la autonomía del coche.

class Car: 
    """Un simple intento de representar un coche.""" 
    def __init__(self, make, model, year): 
        """Inicializa atributos para describir un coche.""" 
        self.make = make
        self.model = model
        self.year = year

class Battery: 
    """Un simple intento de modelar una batería para un coche eléctrico."""
    def __init__(self, battery_size=65): 
        """Inicializa los atributos de la batería.""" 
        self.battery_size = battery_size 
    def describe_battery(self): 
        """Imprime una frase que describe el tamaño de la batería.""" 
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self): 
        """Imprime una frase sobre la autonomía que ofrece esta batería.""" 
        if self.battery_size == 40:
            range = 150 
        elif self.battery_size == 65: 
            range = 225 
        return f"This car can go about {range} miles on a full charge.\n"
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            
class ElectricCar(Car): 
    """Representa aspectos de un coche propios de los vehículos eléctricos."""
    def __init__(self, make, model, year): 
        """ Inicializa los atributos de la clase base. Luego inicializa los 
        atributos específicos de un coche eléctrico. """ 
        super().__init__(make, model, year) 
        self.battery = Battery() 
        
car1 = ElectricCar('nissan', 'leaf', 2024)
car1.battery.get_range()
car1.battery.upgrade_battery()

print(car1.battery.battery_size)
print(car1.battery.get_range())


#9-13. Dados: Haga una clase Dados con un atributo llamado caras, que tenga un 
#       valor predeterminado de 6. Escriba un método llamado tirar_dado() que 
#       imprima un número aleatorio entre 1 y el número de caras que tenga el
#       dado. Haga un dado de 6 caras y tírelo 10 veces. Haga un dado de 10 
#       caras y otro de 20. Lance cada dado 10 veces.

print("\n9.13\n")
from random import randint

class Caras:
    def __init__(self,caras):
        self.caras = caras
        
    def tirar_dado(self):
        print(randint(1,self.caras))

dado6 = Caras(6)
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()
dado6.tirar_dado()

dado10 = Caras(10)
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()
dado10.tirar_dado()

dado20 = Caras(20)
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()
dado20.tirar_dado()

#9-14. Lotería: Cree una lista o tupla que contenga series de 10 números y 5 
#       letras. Seleccione aleatoriamente cuatro números o letras de la lista e
#       imprima un mensaje diciendo que cualquier boleto con estos cuatro 
#       números o letras está premiado.
print("\n9.14\n")

from random import choice

lista = ['a','b','c','d','e',1,2,3,4,5,6,7,8,9,0]

c1 = choice(lista)
c2 = choice(lista)
c3 = choice(lista)
c4 = choice(lista)

print(f"Cualquier série con cualquiera de los caracteres: {c1}, {c2}, {c3}, {c4}, está premiado\n")

#9.15. Análisis de la lotería: Puede usar un bucle para ver lo difícil que sería
#       ganar el tipo de lotería que acaba de modelar. Haga una lista o tupla 
#       llamada mi_boleto. Escriba un bucle que saque números hasta que gane su
#       boleto. Imprima un mensaje que indique cuántas veces ha tenido que
#       ejecutarse el bucle hasta que ha salido el número ganador.

print("\n9.15\n")
from random import choice

lista = ['a','b','c','d','e',1,2,3,4,5,6,7,8,9,0]
mi_boleto = []
n = 0
premiado = 'e642'

while  mi_boleto != premiado:
    c1 = choice(lista)
    c2 = choice(lista)
    c3 = choice(lista)
    c4 = choice(lista)
    if f"{c1}{c2}{c3}{c4}" == 'e642':
        mi_boleto.append(f"{c1}{c2}{c3}{c4}")
        break
    n += 1
    
print(mi_boleto)
print(n)
    







