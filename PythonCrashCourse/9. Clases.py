class Dog:
    """Un intento sencillo de modelar un perro.""" 
    
    def __init__(self, name, age):
        """Inicializa los atributos de nombre y edad.""" 
        self.name = name 
        self.age = age 
    def sit(self): 
        """Simula un perro sentándose en respuesta a una orden.""" 
        print(f"{self.name} is now sitting.") 
    def roll_over(self):
        """Simula hacer la croqueta en respuesta a una orden."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3) 
print(f"My dog's name is {my_dog.name}.") 
print(f"My dog is {my_dog.age} years old.") 
my_dog.sit() 
print(f"\nYour dog's name is {your_dog.name}.") 
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()

class Car: 
    """Un simple intento de representar un coche.""" 
    def __init__(self, make, model, year): 
        """Inicializa atributos para describir un coche.""" 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo con el formato adecuado."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title() 
    def read_odometer(self): 
        """Imprime una oración que indica el kilometraje del coche.""" 
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Configura el kilometraje con el valor dado.""" 
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles): 
        """Añade la cantidad dada a la lectura del cuentakilómetros."""
        self.odometer_reading += miles
    def fill_gas_tank(self):
        """Los coches eléctricos no tienen depósito de combustible.""" 
        print("as Tank FULL")


my_new_car = Car('audi', 'a4', 2024) 
print(my_new_car.get_descriptive_name()) 
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_new_car.odometer_reading = 23 
my_new_car.read_odometer()

my_new_car.update_odometer(55)
my_new_car.update_odometer(35)
my_new_car.read_odometer()

print("\nUsed Car:\n")
my_used_car = Car('subaru', 'outback', 2019) 
print(my_used_car.get_descriptive_name()) 
my_used_car.update_odometer(23_500) 
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

class ElectricCar(Car): 
    """Representa aspectos de un coche propios de los vehículos eléctricos."""
    def __init__(self, make, model, year): 
        """ Inicializa atributos de la clase base. Luego inicializa atributos 
        propios de un coche eléctrico. """ 
        super().__init__(make, model, year) 
        self.battery_size = 40 
    def describe_battery(self): 
        """Imprime una frase que describe el tamaño de la batería."""
        print(f"This car has a {self.battery_size}-kWh battery.") 
    def fill_gas_tank(self):
        """Los coches eléctricos no tienen depósito de combustible.""" 
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name()) 
my_leaf.describe_battery()
my_leaf.fill_gas_tank()

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
        print(f"This car can go about {range} miles on a full charge.\n")

class ElectricCar(Car): 
    """Representa aspectos de un coche propios de los vehículos eléctricos."""
    def __init__(self, make, model, year): 
        """ Inicializa los atributos de la clase base. Luego inicializa los 
        atributos específicos de un coche eléctrico. """ 
        super().__init__(make, model, year) 
        self.battery = Battery() 
        
my_leaf = ElectricCar('nissan', 'leaf', 2024) 
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


"""Una clase que se puede usar para representar un coche."""

class Car: 
    """Un simple intento de representar un coche."""
    def __init__(self, make, model, year): 
        """Inicializa atributos para describir un coche.""" 
        self.make = make 
        self.model = model
        self.year = year 
        self.odometer_reading = 0 
    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo con un formato adecuado."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()
    def read_odometer(self): 
        """Imprime una frase que indica el kilometraje del coche.""" 
        print(f"This car has {self.odometer_reading} miles on it.") 
    def update_odometer(self, mileage): 
        """ Establece la lectura del cuentakilómetros en el valor dado. Rechaza
        el cambio si intenta hacer retroceder el cuentakilómetros. """
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer!") 
    def increment_odometer(self, miles):
        """Suma la cantidad dada a la lectura del cuentakilómetros.""" 
        self.odometer_reading += miles

