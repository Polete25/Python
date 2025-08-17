#6-1.   Persona: Use un diccionario para almacenar información sobre una persona
#       que conozca. Guarde su nombre, apellido, edad y la ciudad en la que
#       vive. Debería tener claves como nombre, apellido, edad y ciudad.
#       Imprima toda la información almacenada en su diccionario. 

persona = { 'Nombre' : 'David' ,
           'Appellido':'Monterrubio' ,
           'Edad' : 29,
           'Ciudad' : 'Barcelona' , 
           }

for clave,valor in persona.items():
    print(f"{clave} : {valor}")

#​6-2.   Números favoritos: Use un diccionario para guardar los números favoritos
#       de distintas personas. Piense en cinco nombres y úselos como claves en 
#       su diccionario. Piense el número favorito de cada persona y guárdelo
#       como valor en su diccionario. Imprima el nombre y el número favorito de
#       cada persona. Para que sea más divertido, puede preguntar a sus amigos 
#       para conseguir datos reales para su programa. 

num_fav = {
    'David' : 10,
    'Rodri' : 9,
    'Koki' : 5,
    'Javi' : 100,
    'Pol' : 25,
    'Nico' : 12,
    }
print(num_fav['Rodri'])
print(num_fav['David'])
print(num_fav['Nico'])

#​6-3.   Glosario: Puede usar un diccionario de Python para modelar un 
#       diccionario real. Sin embargo, para evitar confusiones, lo llamaremos 
#       "glosario". 
#           •​Piense en cinco palabras de programación que haya aprendido en los
#           capítulos anteriores y úselas como claves en su glosario. Guarde sus
#           significados como valores. 
dic_prog = {
    'get' : 'Por si no existe',
    'sum' : 'Sumar numeros',
    'if' : 'Crear condición',
    'else' : 'Cuando no se crea la condición del if',
    'elif' : 'Para cuando hay + de 1 condición',
    }
#           •​Imprima cada palabra con su significado en una salida con formato 
#           limpio. Podría imprimir la palabra seguida de dos puntos y luego la 
#           definición, o la palabra en una línea y la definición sangrada en 
#           una segunda línea. Use el carácter de nueva línea (\n) para insertar
#           una línea en blanco entre cada par palabra-definición en la salida.

print(f'get: {dic_prog['get']}')
print(f'sum: {dic_prog['get']}')
print(f'if: {dic_prog['get']}')
print(f'else: {dic_prog['get']}')
print(f'elif: {dic_prog['get']}')
    
#6-4.   Glosario 2: Ahora que sabe cómo pasar en bucle por un diccionario, 
#       limpie el código del ejercicio 6-3 sustituyendo las llamadas a print() 
#       por un bucle que pase por las claves y valores del diccionario. Cuando
#       sepa con seguridad que su bucle funciona, añada a su glosario cinco
#       términos más relacionados con Python. Cuando vuelva a ejecutar el 
#       programa, estas nuevas palabras y definiciones deberían incluirse
#       automáticamente en la salida. 


for palabra , definicion in dic_prog.items():
    print(f"\n{palabra}: {definicion}")

dic_prog = {'for' : 'Bucle'}

for palabra , definicion in dic_prog.items():
    print(f"\n{palabra}: {definicion}")
 
 
#​6-5.  Ríos: Haga un diccionario con tres ríos importantes y el país por el que
#      discurre cada uno. Un par clave-valor podría ser 'nilo': 'egipto'.

rios = {
    'España' : 'Duero' ,
    'Argentina' : 'Parana',
    'Perú' : 'Amazonas'
    }
 
#           •​Use un bucle para imprimir una frase sobre cada río, como "El Nilo
#           discurre por Egipto". 
# 

for pais,rio in rios.items():
    print(f'El rio {rio} se encuentra en {pais}')

#           •​Use un bucle para imprimir el nombre de cada río incluido en el
#           diccionario. 

for rio in rios.values():
    print(rio.title())

#           •​Use un bucle para imprimir el nombre de cada país incluido en el
#           diccionario. 

for pais in rios.keys():
    pais = pais.title()
    print(pais)

print(f'\n----\m')
#​6-6.  Sondeos: Use el código de favorite_languages.py. 
favorite_languages = { 
    'Jen': 'python',
    'Sarah': 'c++', 
    'Edward': 'rust', 
    'Phil': 'python', 
    'Pol' : 'python',
    }
#           •​Haga una lista de personas que deberían hacer la encuesta sobre 
#           lenguajes preferidos. Incluya algunos nombres que estén ya en el
#           diccionario y otros que no lo estén.

lista = ['Carlos','Nicolas','Chris','Pablo','Sarah','Diego']
 
#           •​Pase en bucle por la lista de personas que deberían hacer la 
#           encuesta. Si ya la han hecho, deles las gracias por responder. Si 
#           todavía no la han completado, imprima un mensaje invitándoles a 
#           hacerlo.

for name in lista:
    if name in favorite_languages:
        print(f'{name} gracias por hacer la encuesta. {favorite_languages[name]}')
    else:
        print(f'{name}, porfavor, realize la encuesta.')

#6-7.   Personas: Empiece con el programa que ha escrito para el ejercicio 6-1.
#       Cree dos diccionarios nuevos que representen a distintas personas y 
#       guarde los tres diccionarios en una lista llamada personas. Pase en 
#       bucle por la lista. Al hacerlo, imprima todo lo que sabe sobre cada 
#       persona. 

persona0 = { 'Nombre' : 'David' ,
           'Apellido':'Monterrubio' ,
           'País' : 'España',
           'Edad' : 29,
           }
persona1 = {'Nombre' : 'Pol',
            'Apellido' : 'Alomar',
            'País' : 'Argentina',
            'Edad' : 30
            }
persona2 = {'Nombre' : 'Paco',
            'Apellido' : 'Sanchez',
            'País' : 'Español',
            'Edad' : 33
            }

personas = (persona0,persona1,persona2)
            
for persona in personas:
    nombre = persona['Nombre']
    apellido = persona['Apellido']
    print(f"Nombre completo: {nombre} {apellido}")
    for clave, valor in persona.items():
        if clave != 'Nombre' and clave != 'Apellido':
            print(f"{clave}: {valor}")
    print()  
 
#​6-8.   Mascotas: Cree varios diccionarios, cada uno representando una mascota 
#       diferente. En cada diccionario, incluya el tipo de animal y el nombre 
#       del dueño. Guarde estos diccionarios en una lista llamada mascotas. 
#       A continuación, pase en bucle por la lista y, al hacerlo, imprima todo 
#       lo que sabe sobre cada mascota. 

mascota0 = {'Dueño' : 'Nico',
            'Animal' : 'Perro',
            'Nombre' : 'Bagui',
            'Edad' : 1
            }
mascota1 = {'Dueño' : 'Mario',
            'Animal' : 'Perro',
            'Nombre' : 'Taco',
            'Edad' : 3
            }
mascota2 = {'Dueño' : 'Pol',
            'Animal' : 'Perro',
            'Nombre' : 'Fox',
            'Edad' : 15
            }

mascotas = (mascota0,mascota1,mascota2)

for mascota in mascotas:
    for clave,valor in mascota.items():
        print(f"{clave}: {valor}")

#​6-9.   Lugares favoritos: Cree un diccionario llamado lugares_favoritos. Piense
#       en tres nombres para usar como claves en el diccionario y guarde entre 
#       uno y tres lugares favoritos para cada persona. Para hacer este 
#       ejercicio un poco más interesante, pregunte a algunos amigos por sus 
#       sitios preferidos. Pase en bucle por el diccionario e imprima el nombre
#       y el lugar favorito de cada persona.

lugares_favoritos = {'Pol' : 'Oceano' ,
                     'Carlos' : 'Club',
                     'Adriana' : 'Gym',
                     'Nico' : 'Cancha',}

for clave,valor in lugares_favoritos.items():
    print(f'El lugar favorito de {clave} es {valor}')

#​6-10.  Números favoritos: Modifique el programa del ejercicio 6-2 para que cada 
#       persona pueda tener más de un número favorito. Luego, imprima el nombre 
#       de cada persona junto con su(s) número(s) favorito(s). 

numeros_favoritos = {'Pol' : ['25','3'] ,
                     'Carlos' : ['59','10'],
                     'Adriana' : ['60'],
                     'Nico' : ['12'],
                     }

for clave,valor in numeros_favoritos.items():
    if len(valor) == 1:
        print(f"El numero favorito de {clave} es: {', '.join(valor)}")
    else:
        print(f"Los numeros favoritos de {clave} son:")
        for num in valor:
            print(num)
 
#​6-11.  Ciudades: Cree un diccionario llamado ciudades. Use los nombres de tres 
#       ciudades como claves en su diccionario. Cree un diccionario de 
#       información sobre cada ciudad e incluya el país en el que se encuentra, 
#       su población aproximada y alguna curiosidad sobre la ciudad. Las claves
#       para cada ciudad serían país, población y curiosidad. Imprima el nombre
#       de cada ciudad y toda la información que tenga guardada sobre ella.

ciudades = {
    'Barcelona' : {
        'país' : 'España',
        'población' : '1.600.000', 
        'curiosidad' : 'Catalan',
    },
    'Rosario' : {
        'país' : 'Argentina',
        'población' : '1.300.000', 
        'curiosidad' : 'Español',
    },
    'Melbourne' : {
        'país' : 'Australia',
        'población' : '5.000.000', 
        'curiosidad' : 'Inglés',
    }
}

for clave, valor in ciudades.items():
    print(clave)
    for clave,valor in valor.items():
        print(f"{clave} : {valor}")


