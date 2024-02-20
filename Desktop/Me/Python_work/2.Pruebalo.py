# 2-1.  Mensaje simple: Asigne un mensaje a una variable e imprima ese mensaje.

message1 = 'Bagui G U A P A'
print(f"\n"+message1)

# 2-2.  Mensajes simples: Asigne un mensaje a una variable e imprímalo.
#       Luego, cambie el valor de la variable por un mensaje diferente e imprima el nuevo mensaje.

message1 = 'Bagui G U A P A'
print(f"\n"+message1)

message1 = 'Bagui GUAPA'
print(f"\n"+message1)

#2-3.   Mensaje personal: Use una variable para representar el nombre de una persona e imprima 
#       un mensaje para esa persona. El mensaje debería ser sencillo, por ejemplo:
#       "Hola, Eric, ¿te gustaría aprender Python hoy?".

nombre = 'Juan Pablo'
print(f"\nQue haces "+nombre+"?")

#2-4.   Grafía de nombres: Use una variable para representar el nombre de una persona e imprima 
#       ese nombre en minúsculas, mayúsculas y con mayúscula inicial.

yo = 'Pol Alomar Casá'
print(f"\n"+yo.lower())
print(f"\n"+yo.upper())
print(f"\n"+yo.title())

#2-5    Cita celebre: Find a quote from a famous person you admire. Print the quot and the name of its author.

print(f"\n"+"Rousseau once said: \"The human is good by nature\"")


#2-6.   Cita célebre 2: Repita el ejercicio 2-5, pero, esta vez, represente el nombre de la persona 
#       usando una variable llamada famous_person. Después, componga el mensaje y represéntelo con 
#       una nueva variable llamada message. Imprima su mensaje.

famous_person = 'Jean-Jacques Rousseau'
message2 = 'The human is good by nature'
print(f"\n"+famous_person+f": "+message2)

#2-7.   Eliminar espacios de nombres: Use una variable para representar el nombre de una persona 
#       e incluya algunos caracteres de espacio en blanco al principio y al final del nombre. 
#       Asegúrese de usar cada combinación de caracteres, "\t" y "\n", al menos una vez. 
#       Imprima el nombre una vez, de modo que se muestren los espacios de alrededor. 
#       A continuación, imprima el nombre usando cada una de las tres funciones que hemos visto: 
#       lstrip(), rstrip() y strip().

nam = '    Nicolas Alomar  '
print(f"\n"+nam)
print(f"\n"+nam.lstrip())
print(f"\n"+nam.rstrip())
print(f"\n"+nam.strip())

#2-8.   Extensiones de archivos: Python cuenta con el método removesuffix(), que funciona exactamente 
#       igual que el método removeprefix(). Asigne el valor 'python_notes.txt' a una variable llamada 
#       filename. A continuación, utilice el método removesuffix() para mostrar el nombre de archivo
#       sin la extensión de archivo, como ocurre con algunos exploradores de archivo.

fileName = 'Python_notes.txt'
print(f"\n"+fileName.removesuffix('.txt')+f"\n")