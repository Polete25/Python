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
