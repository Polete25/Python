#3-1.   Nombres: Guarde los nombres de unos cuantos amigos en una lista llamada nombres. 
#       Imprima el nombre de cada persona accediendo al elemento correspondiente de la lista, 
#       de uno en uno.
amigos = ['David','Oscar','Pablo','Podga','Pol','Quim','Rodri']
print(amigos)
print(amigos[0])
print(amigos[1])
print(amigos[2])
print(amigos[3])
print(amigos[4])
print(amigos[-2])
print(amigos[-1])

#3-2.   Saludos: Empiece con la lista del ejercicio 3-1, pero, en vez de solo imprimir 
#       el nombre de cada persona, imprímales un mensaje. El texto debería ser el mismo,
#       pero cada mensaje debería personalizarse e incluir el nombre de la persona. 
message = 'Que tal '

print(f'\n'+message+amigos[0])
print(f'\n'+message+amigos[1])
print(f'\n'+message+amigos[2])
print(f'\n'+message+amigos[3])
print(f'\n'+message+amigos[4])
print(f'\n'+message+amigos[-2])
print(f'\n'+message+amigos[-1])

#​3-3.  Su propia lista: Piense en su medio de transporte favorito, como la moto o el coche,
#       y haga una lista que incluya varios ejemplos. Use la lista para imprimir una serie
#       de frases sobre esos elementos, como "Me gustaría tener una moto Honda".

motos = ['Honda CBR','Kawasaki 800','Triumph Scramble','Triumph Speed','Suzuki SV650']
quiero = 'Quiero comprarme una '

print(f'\n'+quiero+motos[0])
print(f'\n'+quiero+motos[1])
print(f'\n'+quiero+motos[2])
print(f'\n'+quiero+motos[3])
print(f'\n'+quiero+motos[4])

#3-4.   Lista de invitados: Si pudiese invitar a cualquiera, vivo o muerto, a cenar, ¿a quién invitaría?
#       Haga una lista de al menos tres personas a las que le gustaría invitar a una cena y úsela para
#       imprimir un mensaje para cada persona invitándole a cenar. 

#•​3-5.  Cambiar la lista de invitados: caba de enterarse de que uno de sus invitados no podrá asistir, 
#       así que tiene que enviar un nuevo juego de invitaciones. Tendrá que pensar en otra persona para invitar. 
#           •​Empiece con el programa del ejercicio 3-4. Añada una llamada a print() al final del programa 
#           indicando el nombre del invitado que no puede asistir. 
#           •​Modifique la lista sustituyendo el nombre del invitado que no puede venir por el de otra persona
#           a la que va a invitar en su lugar. 
#           •​Imprima un segundo grupo de mensajes de invitación, uno para cada persona que haya en la lista ahora.

#​3-6.  Más invitados: Acaba de encontrar una mesa más grande, así que dispone de más espacio. 
#       Piense en otros tres invitados más.
#           •​Empiece con el programa del ejercicio 3-4 o 3-5. Añada una llamada a print() al final 
#           para informar a la gente de que ha encontrado una mesa de comedor más grande. 
#           •​Use insert() para añadir un nuevo invitado al principio de la lista. 
#           •​Use insert() para añadir un nuevo invitado en mitad de la lista. 
#           •​Use append() para añadir un nuevo invitado al final de la lista. 
#           •​Imprima un nuevo juego de mensajes de invitación, uno para cada persona de la lista. 

#​3-7.  Reducir la lista de invitados: Acaba de descubrir que la mesa no llegará a tiempo para la cena 
#       y solo tiene espacio para dos invitados. 
#           •​Empiece con el programa de 3-6. Añada una línea que imprima un mensaje diciendo que solo
#           puede invitar a dos personas a cenar. 
#           •​Use pop() para eliminar invitados de la lista de uno en uno hasta que solo queden dos. 
#           Cada vez que retire un nombre de la lista, imprima un mensaje para esa persona diciendo 
#           que lo siente, pero que no puede invitarle a cenar. 
#           •​Imprima un mensaje para cada una de las dos personas que quedan en la lista informándoles 
#           de que siguen invitados. 
#           •​Use del para borrar los dos últimos nombres de la lista y que se quede vacía. 
#           Imprima la lista para asegurarse de que realmente tiene una lista vacía al final del programa.

