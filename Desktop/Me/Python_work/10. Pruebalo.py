#   10-1. Aprender Python: Abra un archivo nuevo en su editor de texto y escriba
#       unas líneas resumiendo lo que ha aprendido sobre Python hasta ahora. 
#       Empiece cada línea con la frase "En Python se puede...". Guarde el 
#       archivo como aprender_python.txt en el mismo directorio que los
#       ejercicios de este capítulo. Escriba un programa que lea el archivo e 
#       imprima dos veces lo que ha escrito: una vez leyendo el archivo completo
#       y otra pasando en bucle por el objeto del archivo. 

from pathlib import Path
path = Path('Prueba.txt')
texto = path.read_text().rstrip()
print(texto)

lines = texto.splitlines()
for line in lines:
    print(line)

# •​10-2. Aprender C: Puede usar el método replace() para sustituir cualquier
#       palabra de una cadena por otra diferente. Aquí tiene un ejemplo rápido 
#       para cambiar 'perro' por 'gato' en una oración: 
#       >>> message = "Me encantan los perros."
#       >>> message.replace('perro', 'gato')
#       'Me encantan los gatos.' 
#       Lea cada línea del archivo que acaba 
#       de crear, aprender_python.txt, y cambie la palabra Python por el nombre
#       de otro lenguaje, como C. Imprima en la pantalla las líneas modificadas.

texto_r = texto.replace('Python','SQL') 
print(texto_r)
 
# •​10-3. Un código más sencillo: El programa file_reader_py en esta sección 
#       utiliza una variable temporal, lines, para mostrar el funcionamiento de
#       splitlines(). Puede saltarse la parte de la variable temporal y pasar un
#       bucle directamente por la lista que devuelve splitlines(): 
#       for line in contents.splitlines():
#       Elimine la variable temporal de cada uno de los programas en esta
#       sección para hacerlos más concisos.

for line in texto_r.splitlines():
    print(line)

#10-4. Invitado: Escriba un programa que pida al usuario su nombre. Cuando 
#       responda, escriba su nombre en un archivo llamado invitado.txt. 

"""
nombre = input("Cual es tu nombre?") 
path = Path('invitado.txt')
path.write_text(nombre)
""" 

#​10-5. Libro de invitados: Escriba un bucle while que pida a los usuarios su
#       nombre. Recopile todos los nombres introducidos por los usuarios y a
#       continuación escríbalos en un archivo llamado libro_invitados.txt. 
#       Asegúrese de que cada entrada aparece en una nueva línea del archivo.

path = Path('lista_invitado.txt')
nombre = ''
lista = ''
while nombre != 'none':
    nombre = input("Cual es tu nombre?") 
    lista += nombre + '\n'
    path.write_text(lista)
    
# 10-6. Suma: Un problema habitual cuando se pide entrada numérica se da cuando 
#       la gente proporciona texto en vez de números. Cuando intentamos 
#       convertir la entrada en un entero, obtenemos un ValueError. Escriba un 
#       programa que solicite dos números, súmelos e imprima el resultado. 
#       Capture el ValueError si cualquiera de los valores de entrada no es un
#       número e imprima un error inteligible para el usuario. Pruebe el 
#       programa introduciendo dos números y luego escribiendo texto en vez de
#       un número.

try:
    numero1 = int(input("Eliga un numero"))
    numero2 = int(input("Eliga orto numero"))
except:
    pass
try:
    print(numero1 + numero2)
except:
    print("Solo con numeros")



