#4-1.   Pizzas: Piense en al menos tres de sus pizzas favoritas.
#       Guarde estos nombres en una lista y use un bucle for para imprimir el 
#       nombre de cada pizza. 
#           •​Modifique su bucle for para imprimir una oración usando el nombre
#           de la pizza en vez de solo el nombre.
#           Para cada pizza debería tener al menos una línea de salida con una 
#           oración simple, como "Me gusta la pizza de pepperoni". 
pizzas = ['Funghi','Peperoni','Rucula']
for pizza in pizzas:
    print(f"\nMe gusta la pizza de {pizza.title()}")    
    
#           •​Añada una línea al final del programa, fuera del bucle, que indique cuánto le gusta la pizza. 
#           La salida debería tener tres o más líneas sobre sus pizzas favoritas y al final una frase adicional,
#           como "¡Me encanta la pizza! 

print("\nMe encanta la pizza\n")

#​4-2.  Animales: Piense en al menos tres animales diferentes que tengan una característica en común. 
#      Guarde los nombres de estos animales en una lista y use un bucle for para imprimir el nombre de cada animal. 

animales = ['Perro','Gato','Delfin']
for animal in animales:
    print(animal)
    
#           •​Modifique su programa para imprimir una oración sobre cada animal, 
#           como "Un perro sería una excelente mascota". 

print(f"\nAlgún día voy a tener 2 {animales[0]}s")
print(f"\nCapaz que voy a tener 1 {animales[1]}")
print(f"\nCreo que en otra vida fui un {animales[2]}")

#           •​Añada una línea al final del programa diciendo qué tienen estos animales en común. Podría imprimir

print("\nTodos ellos son mamíferos\n")

#4-3.   Contar hasta veinte: Use un bucle for para imprimir los números del 1 al 20, ambos incluidos. 

for numero in range(0,21):
    print(numero)

#​4-4.   Un millón: Haga una lista de números de uno a un millón y luego use un bucle for para 
#       imprimir los números. (Si la salida tarda mucho, deténgala pulsando Control-C o cerrando la ventana de salida). 

unmillon = [value*1 for value in range(0,10000000)]
#print(unmillon) 


#​4-5.   Sumar un millón: Haga una lista de los números del uno al millón y use min() y max() para asegurarse
#       de que su lista empieza realmente en uno y acaba en un millón. Utilice también la función sum()
#       para ver lo rápido que Python puede sumar un millón de números.

print(sum(unmillon))
print(max(unmillon))
print(min(unmillon))

#4-6.   Números impares: Use el tercer argumento de la función range() para hacer una lista de 
#       los números impares comprendidos entre 1 y 20. Utilice un bucle for para imprimir cada número. 

impares = list(range(1, 20, 2)) 
print(impares)
for impar in impares:
    print(impar)

#​4-7    Treses: Haga una lista de los múltiplos de 3 comprendidos entre el 3 y el 30. Use un bucle for 
#       para imprimir los números de la lista. 

treses = list(range(0, 30, 3)) 
for tres in treses:
    print(tres)
 
#​4-8.   Cubos: Un número elevado a la tercera potencia es un cubo. Por ejemplo, el cubo de 2 se escribe 
#       como 2**3 en Python. Haga una lista de los 10 primeros cubos (es decir, el cubo de cada entero entre 1 y 10)
#       y use un bucle for para imprimir el valor de cada cubo. 

cubos = [cubo**3 for cubo in range(0,11)]
for cubo in cubos:
    print(cubo)

#4-9.   Comprensión de cubos: Use una lista por comprensión de los 10 primeros cubos.

#?????

#4-10.  Trozos: Partiendo de uno de los programas que hemos escrito en este capítulo, 
#       añada varias líneas al final que hagan lo siguiente: 
#           •​Imprimir el mensaje "Estos son los tres primeros elementos de la lista:".
#           A continuación, use un trozo para imprimir los tres primeros elementos de la lista de ese programa.

print(f"\nEstos son los 3 primeros elementos de la lista:")
print(treses[:3])
for tres in treses[:3]:
    print(tres)
 
#           •​Imprimir el mensaje "Estos tres elementos están en el medio de la lista:".A continuación, use un 
#           trozo para imprimir los tres elementos centrales de la lista.

print(f"\nEstos son los 3 elementos centrales de la lista:")
print(treses[2:5])

#           •​Imprimir el mensaje "Estos son los tres últimos elementos de la lista:". A continuación,
#           use un trozo para imprimir los tres últimos elementos de la lista. 

print(f"\nEstos son los tres últimos elementos de la lista:")
print(treses[-3:])

#​4-11.  Mis pizzas, sus pizzas: Empiece con el programa del ejercicio 4-1. Haga una copia de la lista de
#       pizzas y llámela friend_pizzas. A continuación, haga lo siguiente: 

friend_pizzas = pizzas[:]

#           •​Añada una pizza nueva a la lista original. 

pizzas.append('Margharita')

#           •​Añada una pizza diferente a la lista friend_pizzas. 

friend_pizzas.append('Fetuccini')

#           •​Compruebe que tiene dos listas separadas. Imprima el mensaje "Mis pizzas favoritas son:"
#           y luego use un bucle for para imprimir la primera lista. Imprima el mensaje "Las pizzas 
#           favoritas de mi amigo son:" y después utilice un bucle for para imprimir la segunda lista. 
#           Asegúrese de que cada pizza se guarda en la lista adecuada.

print("\nMis pizzas favoritas sin:")
print(pizzas)
print("\nLas pizzas favoritas de mi amigo son:")
for pizza in friend_pizzas:
    print(pizza)
 
#​4-12.  Más bucles: Todas las versiones de foods.py de esta sección han evitado usar bucles for al imprimir 
#       para ahorrar espacio. Elija una versión de foods.py y escriba dos bucles para imprimir cada lista de comida.

my_foods = ['pizza', 'falafel', 'carrot cake'] 
for food in my_foods:
    print(food)


#4-13.  Bufé: Un restaurante de tipo bufé ofrece solo cinco comidas básicas. Piense en cinco platos básicos 
#       y guárdelos en una tupla. 
#           •​Use un bucle for para imprimir cada comida que ofrece el restaurante. 

platos = ('Macarrones','Pizza bolognesa','Callos','Bravas','Boquerones')
for plato in platos:
    print(plato)

#           •​Intente modificar alguno de los elementos y asegúrese de que Python rechaza el cambio.

#platos[1]='Tapas varias' ERROR
 
#           •​El restaurante cambia su menú, sustituyendo dos elementos por comidas diferentes. Añada una línea 
#           que rehaga la tupla y use un bucle for para imprimir cada uno de los elementos del menú modificado.

platos = ('Macarrones','Carpaccio','Cesar','Bravas','Boquerones')
for plato in platos:
    print(plato)

#•​4-14. PEP 8: Eche un vistazo a la guía de estilo original (en inglés) de la PEP 8, 
#       en https://python.org/dev/peps/pep-0008/. Todavía no le dará un gran uso, pero no está de más echarle un vistazo. 
# 
#•​4-15. Revisión de código: Elija tres de los programas que ha escrito en este capítulo y modifíquelos para ajustarlos 
#       a la PEP 8: 
#           •​Use cuatro espacios por cada nivel de sangrado. Configure el editor de texto para insertar cuatro 
#           espacios cada vez que pulse Tab, si es que no lo ha hecho ya (consulte el apéndice B si necesita instrucciones). 
#           •​Use menos de 80 caracteres en cada línea y configure su editor para que muestre una guía vertical en 
#           la posición del 80º carácter. 
#           •​No abuse de las líneas en blanco en sus archivos de programa.

# D O N E
