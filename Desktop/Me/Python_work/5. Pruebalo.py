#5-1.   Pruebas condicionales: Escriba una serie de pruebas condicionales. 
#       Imprima una frase describiendo cada prueba y su predicción para el 
#       resultado. 
car = 'subaru'
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru') 
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi')

#           •​Examine los resultados y asegúrese de comprender por qué cada 
#           línea se evalúa como True o False. 
#           •​Cree al menos 10 pruebas y haga que 5, como mínimo, se evalúen
#           como True y otras 5 como False. 

name = 'Pol'
age = 30
status = 'lost'
nationality = 'Unokwn'
relationship = 'none'

print(name == 'Carlos')
print(name == 'Pol')
print(age == 'young')
if age > 29:
    print('Old')
print(status == 'improving')
print(relationship == 'married')
print(nationality == 'Russian')

#•5-2.  Más pruebas condicionales: No hace falta que limite el número
#       de pruebas condicionales a diez. Si quiere probar más comparaciones,
#       escriba más pruebas y añádalas a conditional_tests.py. Haga que un 
#       resultado sea True y otro False para cada una de estas pruebas: 
#           •​Pruebas de igualdad y desigualdad con cadenas. 
print(name == 'Pol' and age == 30)
print(status == 'improving' and age < 25)
#           •Pruebas con el método lower(). 
print(name.lower() == 'pol')
#           •​Pruebas numéricas que impliquen igualdad y desigualdad, mayor 
#           que y menor que, mayor o igual que y menor o igual que.
#           •​Pruebas con las palabras clave and y or. 
print(age > 5 and age == 30)
print(age != 5 or age == 23)
#           •​Prueba para comprobar si un elemento está en una lista. 
sports = ['Surf','Football','Basketball','Volleyball','Padel','Tenis']
print('Surf' in sports)
#           •​Prueba para comprobar si un elemento no está en una lista.
print('Surf' not in sports)

#5-3.   Colores de aliens #1: Imagine un alien que acaba de ser derribado en un 
#       juego. Cree una variable llamada color_alien y asígnele como valor 
#       'verde', 'amarillo' o 'rojo'. 
color_alien = 'rojo'
#           •​Escriba una sentencia if para comprobar si el color del alien es 
#           verde. Si lo es, imprima un mensaje informando al jugador de que 
#           ha ganado 5 puntos. 
if color_alien == 'verde':
    print('Has ganado 5 puntos')
#           •​Escriba una versión de este programa que pase la prueba if y otra
#           que no. (La versión que no supera la prueba no tendrá salida).
if color_alien == 'rojo':
    print('Has ganado 15 puntos')
 
#​5-4.  Colores de aliens #2: Elija un color para un alien igual 
#      que en el ejercicio 5-3 y escriba una cadena if-else. 
#           •​Si el color del alien es verde, imprima un mensaje informando al 
#           jugador de que ha ganado 5 puntos por disparar al alien. 
if color_alien == 'verde':
    print('Has ganado 5 puntos')
#           •​Si el color del extraterrestre no es verde, imprima una frase 
#           informando al jugador de que acaba de ganar 10 puntos. 
if color_alien != 'verde':
    print('Has ganado 10 puntos') 
#           •​Escriba una versión de este programa que ejecute el bloque if 
#           y otra que ejecute el bloque else. 
if color_alien == 'verde':
    print('Has ganado 5 puntos')
else:
    print('Has ganado 10 puntos')
#​5-5.  Colores de aliens #3: Convierta la cadena if-else del 
#      5-4 en una cadena if-elif-else. 
#           •​Si el alien es verde, imprima un mensaje diciendo al jugador
#           que ha ganado 5 puntos. 
if color_alien == 'verde':
    print('Has ganado 5 puntos')
#           •​Si el alien es amarillo, imprima un mensaje diciendo al jugador 
#           que ha ganado 10 puntos. 
elif color_alien == 'rojoamarillo':
    print('Has ganado 10 puntos')   
#           •​Si el alien es rojo, imprima un mensaje diciendo al jugador que 
#           ha ganado 15 puntos. 
elif color_alien == 'rojo':
    print('Has ganado 15 puntos')  
#           •​Escriba tres versiones de este programa, asegurándose de que se 
#           imprime cada mensaje para el color de alien adecuado. 
       
#​5-6.  Etapas vitales: Escriba una cadena if-elif-else para 
#      determinar la etapa vital de una persona. Atribuya un valor a la 
#      variable edad y: 
edad = 0
#           •​Si la persona tiene menos de 2 años, imprima un mensaje diciendo
#           que es un bebé. 
if edad < 2:
    print('Bebe')   
#           •​Si la persona tiene entre 2 y 4 años, imprima un mensaje diciendo 
#           que es un niño pequeño. 
elif edad >= 2 and edad < 4:
    print('Niño pequeño')
#           •​Si la persona tiene como mínimo 4 años, pero menos de 13, imprima 
#           un mensaje diciendo que es un niño. 
elif edad >= 4 and edad < 13: 
    print('Niño')
#           •​Si la persona tiene como mínimo 13 años, pero menos de 20, imprima 
#           un mensaje diciendo que es un adolescente. 
elif edad >= 13 and edad < 20: 
    print('Adolescente')       
#           •​Si la persona tiene al menos 20 años, pero no llega a 65, imprima
#           un mensaje diciendo que es un adulto. 
elif edad >= 20 and edad < 65: 
    print('Adulto') 
#           •​Si la persona tiene 65 años o más, imprima un mensaje diciendo que
#           tiene más de 65 años. 
elif edad >= 65: 
    print('+65')   
#​5-7.   Fruta favorita: Haga una lista de sus frutas favoritas y 
#       escriba una serie de sentencias if independientes que comprueben 
#       ciertas frutas en su lista.
#           •​Haga una lista de sus frutas favoritas y llámela frutas_favoritas.
frutas = ['Platano','Naranja','Kiwi']
#           •​Escriba cinco sentencias if. Cada una debería comprobar si una 
#           fruta concreta está en su lista. Si lo está, el bloque if debería
#           imprimir un mensaje como "¡Pues sí que te gustan los plátanos!".
if 'Platano' in frutas:
    print('Pues si que te gustan los platanos')
if 'Manzana' in frutas:
    print('Pues si que te gustan los Manzanas')
else:
    print('Las Manzanas parece que no')
if 'Kiwi' in frutas:
    print('Pues si que te gustan los kiwis')
    
#5-8.   Hola, Admin: Cree una lista de cinco o más nombres de usuario, 
#       incluyendo el nombre 'admin'. Imagine que está escribiendo código que 
#       imprimirá un mensaje para cada usuario cuando inicien sesión en un sitio
#       web. Pase en bucle por la lista e imprima un saludo para cada usuario: 
usuarios = ['Aadmin','Usuario1','Usuario2','Usuario3','Usuario4','Usuario5']           
#           •​Si el nombre de usuario es 'admin', imprima un saludo especial, 
#           como "Hola, admin, ¿quieres ver un informe de estado?". 
if usuarios:
    for usuario in usuarios:
        if usuario == 'Admin':
            print('Hola, admin, ¿Quieres ver un informe de estado?')
#           •​De lo contrario, imprima un saludo genérico, como "Hola, Juan, 
#           gracias por volver a entrar". 
        else: 
            print(f'Hola {usuario}, gracias por volver a entrar')
#5-9.   Sin usuarios: Añada una prueba if al programa del ejercicio anterior
#       (hello_admin.py) para asegurarse de que la lista no está vacía. 
           
#           •​Si la lista está vacía, imprima el mensaje "¡Necesitamos encontrar
#           algún usuario!". 
#           •​Borre todos los nombres de usuario de la lista y asegúrese de 
#           que se imprime el mensaje correcto. 
usuarios = []
if usuarios:
    for usuario in usuarios:
        if usuario == 'Admin':
            print('Hola, admin, ¿Quieres ver un informe de estado?')
        else: 
            print(f'Hola {usuario}, gracias por volver a entrar')
else:
    print("Necesitamos encontrar usuarios")
#​5-10.  Comprobar nombres de usuario: Haga lo siguiente para crear un programa 
#       que simule cómo los sitios web se aseguran de que todos los usuarios 
#       tienen un nombre único.            
#           •​Cree una lista con cinco o más nombres de usuario llamada 
#           current_users. 
current_users = ['Pol','Nico','Chirs','Noe','Diego'] 
#           •​Cree otra lista de cinco nombres de usuario llamada new_users.
#           Asegúrese de que uno o dos de los nuevos nombres de usuario estén 
#           también en la lista current_users. 
new_users = ['pol','Carlos','Fox','Adriana','Nicolás'] 
#           •​Pase en bucle por la lista new_users para ver si cada nuevo
#           nombre de usuario está ya usado. Si lo está, imprima un mensaje
#           diciendo al usuario que tendrá que introducir otro nombre. 
#           Si un nombre no se ha usado todavía, imprima un mensaje diciendo 
#           que el nombre de usuario está disponible.
if new_users:
    for new_user in new_users:
        if new_user in current_users:
            print(f"El usuario {new_user} ya está usado.")
        else:
            print("El nombre de usuario está disponible.")
     
#           •​Asegúrese de que su comparación no distingue entre mayúsculas y 
#           minúsculas. Si se ha usado 'Juan', no debería aceptarse 'JUAN'. 
#           (Para hacer esto, necesitará una copia de current_users con la 
#           versión en minúsculas de todos los usuarios existentes). 
lower_current_users = [user.lower() for user in current_users]
if new_users:
    for new_user in new_users:
        if new_user.lower() in lower_current_users:
            print(f"El usuario {new_user} ya está usado.")
        else:
            print("El nombre de usuario está disponible.")
#​5-11. Números ordinales en inglés: Los números ordinales indican su posición 
#       en una lista, como 1º, 2º, etc. En inglés, la mayoría terminan en th, 
#       excepto el 1, el 2 y el 3, que terminan en st, nd y rd, respectivamente. 
#           •​Guarde los números del 1 al 9 en una lista. 
numeros = [1,2,3,4,5,6,7,8,9]
#           •​Pase en bucle por la lista. 
#           •​Use una cadena if-elif-else dentro del bucle para imprimir 
#           la terminación adecuada en inglés de cada número. La salida debería 
#           ser "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", y cada resultado debería 
#           aparecer en una línea separada.
if numeros:
    for numero in numeros:
        if numero == 1:
            print('1st')
        elif numero == 2:
            print('2ns')
        elif numero == 3:    
            print('3rd')
        else:
            print(f"{numero}th")

#5-12.  Dar estilo a sentencias if: Revise los programas que ha escrito en este
#       capítulo y asegúrese de que ha dado el estilo apropiado a sus pruebas
#       condicionales. 
#​5-13.  Sus ideas: Llegados a este punto, ya es un programador más capacitado 
#       que cuando empezó este libro. Ahora que tiene más idea de cómo se 
#       modelan situaciones del mundo real en programas, es posible que ya 
#       esté pensando en problemas a los que podría dar solución con sus 
#       propios programas. Tome nota de cualquier idea que se le ocurra sobre 
#       los problemas que podría interesarle resolver a medida que sus 
#       habilidades de programación mejoran. Piense en los juegos que le 
#       gustaría desarrollar, los conjuntos de datos que quiere explorar o las 
#       aplicaciones web que le gustaría crear.
