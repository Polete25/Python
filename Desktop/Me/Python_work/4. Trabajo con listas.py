magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(f"\n{magician.title()}, that was a great trick!\nI can't wait to see your next trick,{magician.title()}.")
print("\nThank you, everyone. That was a great magic show!\n")


#Numeros!

for value in range(1, 5):
    print(value)
    
for value in range(6):
    print(value)
print("\n")

numbers = list(range(6))
print(numbers)

#Numeros pares del 2 al 10
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)

#Crear todos los cuadrados del 0 al 10:
squares = []
for value in range(0,11):
    square = value **2
    squares.append(square)
print(squares)
#Mejorado:
squares = [] 
for value in range(0,11): 
    squares.append(value**2) 
print(squares)
#aun mejor:
squares = [value**2 for value in range(1, 11)]
print(squares)
#otros comandos útiles:
digits = [1,2,3,4,5,6,7,8,25,34,67] 
print(sum(digits))
print(max(digits))
print(min(digits))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:") 
for player in players[:3]:
    print(player.title())
    
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 
print("My favorite foods are:") 
print(my_foods) 
print("\nMy friend's favorite foods are:") 
print(friend_foods)
my_foods.append('Mashrooms')
friend_foods.append('Tortelini')
print(my_foods)
print(friend_foods)

#Si lo hacemos así
my_foods = friend_foods
#las modificaciones se hacen en las dos
print(my_foods)
print(friend_foods)
my_foods.append('Mashrooms')
print(my_foods)
print(friend_foods)

# Python se refiere a los valores que no pueden cambiar como inmutables, y una lista inmutable se denomina "tupla".
# Igual que la lista pero con parentesis en vez de corchetes:

dimensiones = (200,50)
print(dimensiones)
for dimension in dimensiones:
    print(dimension)

#dimension[0] = 20 ERROR






