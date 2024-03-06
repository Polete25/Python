
#8-1. Mensaje: Escriba una función llamada mostrar_mensaje() que imprima una
#       oración diciendo a todos lo que está aprendiendo en este capítulo. Llame
#       a la función y asegúrese de que el mensaje se muestra correctamente. 
print("8.1")
def mostrar_mensaje(name):
    print(f"{name.title()} estas estudiando mucho")
mostrar_mensaje('Pol')
    

# ​8-2. Libro favorito: Escriba una función llamada libro_favorito() que acepte 
#       un parámetro título. La función debería imprimir un mensaje como "Uno de
#       mis libros favoritos es Alicia en el País de las Maravillas". Llame a la
#       función, asegurándose de incluir el título de un libro como argumento en
#       la llamada a la función.
print("8.2")
def libro_favorito(libro):
    print(f"Mi libro favorito con diferencia es {libro.title()} ")
libro_favorito('El nombre del viento')

#8-3. Camiseta: Escriba una función llamada hacer_camiseta() que acepte una
#       talla y un texto para un mensaje que habría que imprimir en la camiseta.
#       La función debería imprimir una frase resumiendo la talla de la camiseta
#       y el mensaje impreso. Llame a la función una vez con argumentos 
#       posicionales para hacer una camiseta. Llame a la función por segunda vez
#       usando argumentos de palabra clave.
print("8.3")
def hacer_camiseta(talla,texto):
    print(f"Imprimiento camiseta talla {talla} con texto: {texto}")
hacer_camiseta('XL',"'C'est la vie'")    
hacer_camiseta(texto="C'estlavie",talla='XL')
    

# ​8-4. Camisetas grandes: Modifique la función hacer_camiseta () para que las
#       camisetas sean grandes por defecto con un mensaje que diga "Me encanta 
#       Python". Haga una camiseta grande y una mediana con el mensaje 
#       predeterminado y una de cualquier talla con un mensaje diferente.
print("8.4")
def hacer_camiseta(talla='XL',texto=''):
    print(f"Imprimiento camiseta talla {talla} con texto: {texto}")
hacer_camiseta('XL',"'C'est la vie'")    
hacer_camiseta(texto="Viva Python")

 
#​8-5. Ciudades: Escriba una función llamada describir_ciudad() que acepte el
#       nombre de una ciudad y su país. La función debería imprimir una oración
#       simple, como "Reikiavik está en Islandia". Dé al parámetro del país un 
#       valor predeterminado. Llame a la función para tres ciudades diferentes,
#       con al menos una que no esté en el país predeterminado.
print("8.5")
def describir_ciudad(ciudad,pais):
    print(f'{ciudad} se encuentra en {pais}.')
describir_ciudad('Barcelona','España')

#8-6. Nombres de ciudad: Escriba una función llamada ciudad_pais() que admita el
#       nombre de una ciudad y su país. La función debería devolver una cadena 
#       con formato, similar a esta: "Santiago, Chile" Llame a su función con al
#       menos tres pares ciudad-país e imprima los valores devueltos. 
print("8.6")
def describir_ciudad(ciudad,pais):
    print(f'{ciudad}, {pais}.')
describir_ciudad('Barcelona','España')
describir_ciudad('Rosario','Argentina')
describir_ciudad('Brisbane','Australia')

# •​8-7. Álbum: Escriba una función llamada hacer_album() que cree un diccionario
#       para describir un álbum musical. La función debería aceptar un nombre de
#       artista y un título de álbum y debería devolver un diccionario con estas
#       dos informaciones. Use la función para hacer tres diccionarios que 
#       representen distintos álbumes. Imprima cada valor devuelto para
#       comprobar que los diccionarios están almacenando bien la información. 
#       Use None para añadir un parámetro opcional a hacer_album() que permita 
#       guardar el número de canciones que contiene un álbum. Si la línea de 
#       llamada incluye un valor para el número de canciones, añádalo al 
#       diccionario del álbum. Haga al menos una nueva llamada a la función que 
#       incluya este dato.

print("8.7")
def hacer_album(nom_art, tit_alb, n_canc = None):

    if n_canc: 
        alb_mus = {'Nombre Artista': nom_art, 'Titulo Album': tit_alb, 'Numero canciones': n_canc} 
    else: 
        alb_mus = {'Nombre Artista': nom_art, 'Titulo Album': tit_alb} 
    return alb_mus
    

alb_mus1 = hacer_album('Pol','La nena',8)
alb_mus2 = hacer_album('Pablo','Crisalidad',1)
alb_mus3 = hacer_album('Cristian','Fotito')
print(alb_mus1)
print(alb_mus2)
print(alb_mus3)


#8-8. Álbumes de usuarios: Empiece con el programa del ejercicio 8-7. Escriba un
#       bucle while que permita a los usuarios introducir el artista y el título
#       de un álbum. Una vez que disponga de esa información, llame a 
#       hacer_album() con la entrada de usuario e imprima el diccionario que se 
#       ha creado. Asegúrese de incluir un valor para salir en el bucle while.
print("8.8")
def hacer_album(nom_art, tit_alb, n_canc = None):
    if n_canc: 
        alb_mus = {'Nombre Artista': nom_art, 'Titulo Album': tit_alb, 'Numero canciones': n_canc} 
    else: 
        alb_mus = {'Nombre Artista': nom_art, 'Titulo Album': tit_alb} 
    return alb_mus

while True:
    nom_art = input("Nombre artista: ")
    if nom_art == 'q':
        break
    tit_alb = input("Nombre Album: ")
    if tit_alb == 'q':
        break
    n_canc = input("Numero de canciones: ")
    if n_canc == 'q':
        break
    album = hacer_album(nom_art, tit_alb,n_canc)
    print(album)


#8-9. Mensajes: Haga una lista con una serie de mensajes de texto cortos. Pásela
#       a una función llamada mostrar_mensajes() que imprima cada mensaje. 
print("8.9")
def mostar_mensajes(lista):
    while lista:
        msg = lista.pop()
        print(msg)

lista1 = ['Hola','Adios','Que tal']

mostar_mensajes(lista1)
 
# •​8-10. Enviar mensajes: Empiece con una copia del programa del ejercicio 8-9.
#       Escriba una función llamada enviar_mensajes() que imprima cada mensaje 
#       de texto y lo mueva a una nueva lista denominada mensajes_enviados a
#       medida que imprime. Después de llamar a la función, imprima ambas listas
#       para asegurarse de que los mensajes se han movido correctamente.
print("8.10")
def mostar_mensajes(lista,msj_env):
    while lista:
        msg = lista.pop()
        msj_env.append(msg)
    print(lista)
    print(msj_env)
    
lista1 = ['Hola','Adios','Que tal']
msj_env1 = []
mostar_mensajes(lista1,msj_env1)


#8-11. Mensajes archivados: A partir del trabajo realizado para el ejercicio
#       8-10, llame a la función enviar_mensajes() con una copia de la lista de 
#       mensajes. Después, imprima ambas listas para confirmar que la lista 
#       original conserva sus mensajes.
print("8.11")
def mostar_mensajes(lista,msj_env):
    while lista:
        msg = lista.pop()
        msj_env.append(msg)
    print(lista)
    print(msj_env)
    
lista1 = ['Hola','Adios','Que tal']
msj_env1 = []
mostar_mensajes(lista1[:],msj_env1)
print(lista1)

#8-12. Sándwiches: Escriba una función que acepte una lista de elementos que 
#       quiere una persona para un sándwich. La función debería tener un 
#       parámetro que recoja todos los argumentos que le dé la llamada e 
#       imprimir un resumen del sándwich que se está pidiendo. Llame a la 
#       función tres veces, usando un número distinto de argumentos cada vez.
print("8.12\n")
def sandwiches(*toppings):
    print("El sandwich contiene:\n")
    for topping in toppings:
        print(f"- {topping}\n")
sandwiches("Tomate","Lechuga","Mayonesa","Pollo","Huevo")
sandwiches("Tomate","Lechuga","Mayonesa")

 
#8-13. Perfil de usuario: Empiece con una copia de user_profile.py. Haga un 
#       perfil suyo llamando a build_profile(), usando su nombre y apellido y 
#       otros tres pares clave-valor que le describan. 

print("8.13\n")
def build_profile(first, last, **user_info):
    """Crea un diccionario con todo lo que sabemos sobre un usuario.""" 
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    return user_info 

user_profile = build_profile('Pol', 'Alomar', 
                            job='Data Engineer', 
                            status='Unenployed',
                            sport = "Surf")
print(user_profile)

#​8-14. Coche: Escriba una función que guarde información sobre un coche en un 
#       diccionario. Debería recibir siempre un fabricante y un nombre de modelo
#       y aceptar después un número arbitrario de argumentos de palabra clave.
#       Llame a la función con  la información requerida y otros dos pares 
#       nombre-valor, como un color o una prestación opcional. Su función 
#       debería funcionar para una llamada  como esta: car = make_car('subaru', 
#       'outback', color='blue',  tow_package=True) Imprima el diccionario
#       devuelto y asegúrese de que se  ha almacenado bien toda la información.
print("\n8.14\n")
def make_car(modelo,fabricante,**coche_dic):
    coche_dic['modelo'] = modelo
    coche_dic['fabricante'] = fabricante
    return coche_dic

car = make_car('subaru','outback', color='blue',  tow_package=True)
print(car)

#8-15. Imprimir modelos: Ponga las funciones del ejemplo printing_models.py en 
#       un archivo aparte llamado printing_functions.py. Escriba una sentencia 
#       import en la parte superior de printing_models.py y modifique el archivo
#       para usar las funciones importadas. 
print("\n8.15\n")

import Funciones as f

user_profile = f.build_profile('albert', 'einstein', 
                            location='princeton', 
                            field='physics')

#​8-16. Importaciones: Use uno de los programas que haya escrito que contenga una
#       función y guarde esa función en un archivo aparte. Importe la función al
#       archivo de programa principal y llámela con cada una de estas técnicas: 
#       import nombre_módul from nombre_módulo import nombre_función from 
#       nombre_módulo import  nombre_función as nf import nombre_módulo as nm 
#       from nombre_módulo import *

