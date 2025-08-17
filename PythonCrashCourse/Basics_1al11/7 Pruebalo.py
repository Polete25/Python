#7-1.   Coche de alquiler: Escriba un programa que pregunte al usuario qué tipo 
#       de coche desea alquilar. Imprima un mensaje sobre el coche, como "Veamos
#       si tenemos un Subaru para usted". 

#coche = input("Que tipo de coche desea alquilar?")
#print(f"Vamos a ver si tenemos un {coche}")

#​7-2.   Mesa en un restaurante: Escriba un programa que pregunte al usuario 
#       cuántos vienen a cenar. Si la respuesta es más de ocho, imprima un 
#       mensaje diciendo al usuario que tendrán que esperar mesa. De lo 
#       contrario, dígale que su mesa está lista. 

#guesses = input("Cuantos comensales van a ser?")
#guesses = int(guesses)
#if guesses > 8:
#    print("Lo siento, tendrán que esperar.")
#else:
#    print("Perfecto, su mesa está lista")
    
#​7-3.   Múltiplos de diez: Pida al usuario un número y luego infórmele de si ese
#       número es múltiplo de 10 o no.

#numero = input("Inserte un número")
#numero = int(numero)
#if numero % 10 == 0:
#    print("El número es multiplo de 10")
#else:
#    print("El número NO es multiplo de 10")
    
#7-4.   Ingredientes de pizza: Escriba un bucle que pida al usuario que 
#       introduzca una serie de ingredientes de pizza y termine escribiendo el
#       valor 'quit'. Cuando introduzca cada ingrediente, imprima un mensaje 
#       diciendo que lo añadirá a su pizza. 

#prompt = "Que ingrediente quiere?"
#ingrediente = ""
#lista = ""
#while True:
#    ingrediente = input(prompt)
#    if ingrediente != 'quit':
#        print("Ingrediente añadido a su pizza.")
#        lista += ingrediente
#        lista += '\n'
#    else:
#        break
#print(lista)


#​7-5.   Entradas de cine: Un cine cobra las entradas a distinto precio en 
#       función de la edad del espectador. Los menores de 3 años entran gratis,
#       los niños de entre 3 y 12 años pagan 8 euros y la entrada para mayores
#       de 12 años cuesta 12 euros. Escriba un bucle para preguntar a los 
#       usuarios su edad y luego dígales el precio de su entrada. 

#prompt = 'Que edad tiene?'
#edad = ''
#while True:
#    edad = input(prompt)
#    edad = int(edad)
#    if edad < 3 and edad > 0:
#        print('Entra gratis')
#    elif edad >= 3 and edad < 12:
#        print('Le toca pagar 8€')
#    elif edad >= 12:
#        print('Le toca pagar 12€')
#    elif edad == 0:
#        break
    
    

#​7-6.   Tres salidas: Escriba distintas versiones de los ejercicios 7-4 o 7-5, 
#       haciendo cada uno de los siguientes como mínimo una vez: 
#           •​Use una prueba condicional en la sentencia while para detener el 
#           bucle. 
#           •​Use una variable active para controlar cuánto tiempo se ejecuta el 
#           bucle.
#           •​Use una sentencia break para salir del bucle cuando el usuario 
#           introduzca el valor 'quit'. 



#​7-7.   Infinidad: Escriba un bucle que no termine nunca y ejecútelo. (Para 
#       detenerlo, pulse Control-C o cierre la ventana que muestra la salida).

#prompt = 'Guapo'
#while True:
#    print(prompt)


#7-8.   Bocatería: Haga una lista llamada pedidos_bocadillos y rellénela con los
#       nombres de varios bocadillos. A continuación, haga una lista vacía 
#       llamada bocadillos_terminados. Pase en bucle por la lista de pedidos de
#       bocadillos e imprima un mensaje para cada pedido, como "Su bocadillo de 
#       atún está listo". A medida que se hagan los bocadillos, páselos a la 
#       lista de terminados. Cuando todos los bocadillos estén hechos, imprima 
#       un mensaje que los enumere todos. 

#pedidos_bocadillos = ['Tortilla','Sobrasada','Calamares','Sandwich']
#bocadillos_terminados = []

#while pedidos_bocadillos:
#    pedido = input("Que bocadillo quieres pedir?")
#    if pedido in pedidos_bocadillos:
#        pedidos_bocadillos.remove(pedido)
#        bocadillos_terminados.append(pedido)
#    elif pedido not in pedidos_bocadillos:
#        print("No tenemos es bocadillo.")

#print("\n--- Lista bocatas ---") 
#for boca in bocadillos_terminados: 
#    print(f"\n{boca.title()}")

#​7-9.   Ya no hay pastrami: Usando la lista pedidos_bocadillos del ejercicio
#       7-8, asegúrese de que el bocadillo de 'pastrami' aparezca en la lista al
#       menos tres veces. Añada código al principio del programa para imprimir 
#       un mensaje diciendo que no queda pastrami y use un bucle while para
#       eliminar todas las apariciones de 'pastrami' en pedidos_bocadillos.
#       Asegúrese de que no pasa ningún bocadillo de pastrami a la lista 
#       bocadillos_terminados.

#pedidos_bocadillos = ['Tortilla','Pastrami','Sobrasada','Pastrami','Calamares',
#                      'Pastrami','Sandwich']
#bocadillos_terminados = []
#
#print("Lamento informar que no quedan bocadillos pastrami")
#boca = 'Pastrami'
#while boca in pedidos_bocadillos:
#    pedidos_bocadillos.remove(boca)
#
#while pedidos_bocadillos:
#    pedido = input("Que bocadillo quieres pedir?")
#    if pedido in pedidos_bocadillos:
#        pedidos_bocadillos.remove(pedido)
#        bocadillos_terminados.append(pedido)
#    elif pedido not in pedidos_bocadillos:
#        print("No tenemos es bocadillo.")
#
#print("\n--- Lista bocatas ---") 
#for boca in bocadillos_terminados: 
#    print(f"\n{boca.title()}")
 
#​7-10.  Vacaciones de ensueño: Escriba un programa que pregunte a los usuarios
#       por las vacaciones de sus sueños. Escriba unas instrucciones como "Si 
#       pudieras visitar cualquier lugar del mundo, ¿dónde irías?". 
#       Incluya un bloque de código que imprima el resultado de la encuesta.

prompt1 = "Cual es tu nombre?"
prompt2 = "Cuales son las vacaciones de tus sueños?"
usuarios = {}
encuesta = True

while encuesta:
    usuario = input(prompt1)
    vacas = input(prompt2)
    usuarios[usuario]=vacas
    repeat = input("Alguien más va a hacer la encuesta?")
    if repeat == 'No':
        encuesta = False
        
print("\n--- Poll Results ---") 
for name, response in usuarios.items():
    print(f"{name} quier ir a {response}.")
        



