
#8-1. Mensaje: Escriba una función llamada mostrar_mensaje() que imprima una
#       oración diciendo a todos lo que está aprendiendo en este capítulo. Llame
#       a la función y asegúrese de que el mensaje se muestra correctamente. 

def mostrar_mensaje(name):
    print(f"{name.title()} estas estudiando mucho")
mostrar_mensaje('Pol')
    

# ​8-2. Libro favorito: Escriba una función llamada libro_favorito() que acepte 
#       un parámetro título. La función debería imprimir un mensaje como "Uno de
#       mis libros favoritos es Alicia en el País de las Maravillas". Llame a la
#       función, asegurándose de incluir el título de un libro como argumento en
#       la llamada a la función.

def libro_favorito(libro):
    print(f"Mi libro favorito con diferencia es {libro.title()} ")
libro_favorito('El nombre del viento')

#8-3. Camiseta: Escriba una función llamada hacer_camiseta() que acepte una
#       talla y un texto para un mensaje que habría que imprimir en la camiseta.
#       La función debería imprimir una frase resumiendo la talla de la camiseta
#       y el mensaje impreso. Llame a la función una vez con argumentos 
#       posicionales para hacer una camiseta. Llame a la función por segunda vez
#       usando argumentos de palabra clave.

def hacer_camiseta(talla,texto):
    print(f"Imprimiento camiseta talla {talla} con texto: {texto}")
hacer_camiseta('XL',"'C'est la vie'")    
hacer_camiseta(texto="C'estlavie",talla='XL')
    

# ​8-4. Camisetas grandes: Modifique la función hacer_camiseta () para que las
#       camisetas sean grandes por defecto con un mensaje que diga "Me encanta 
#       Python". Haga una camiseta grande y una mediana con el mensaje 
#       predeterminado y una de cualquier talla con un mensaje diferente.

def hacer_camiseta(talla='XL',texto=''):
    print(f"Imprimiento camiseta talla {talla} con texto: {texto}")
hacer_camiseta('XL',"'C'est la vie'")    
hacer_camiseta(texto="Viva Python")

 
#​8-5. Ciudades: Escriba una función llamada describir_ciudad() que acepte el
#       nombre de una ciudad y su país. La función debería imprimir una oración
#       simple, como "Reikiavik está en Islandia". Dé al parámetro del país un 
#       valor predeterminado. Llame a la función para tres ciudades diferentes,
#       con al menos una que no esté en el país predeterminado.

def describir_ciudad(ciudad,pais):
    print(f'{ciudad} se encuentra en {pais}.')
describir_ciudad('Barcelona','España')

