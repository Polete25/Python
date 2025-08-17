
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0['color']) 
print(alien_0['points'])

new_points = alien_0['points'] 
print(f"You just earned {new_points} points!")

print(alien_0) 
alien_0['x_position'] = 0
alien_0['y_position'] = 25 
print(alien_0)

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium','points':10}
print(f"Original position: {alien_0['x_position']}")

# Mueve el alien hacia la derecha.
# Determina cuánto se mueve el alien basándose en su velocidad actual.
if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else: 
# Debe ser un alien rápido. 
    x_increment = 3 
# La nueva posición es la antigua más el incremento.
alien_0['x_position'] = alien_0['x_position'] + x_increment 
print(f"New position: {alien_0['x_position']}")

del alien_0['points']
print(alien_0)

favorite_languages = { 
    'jen': 'python',
    'sarah': 'c++', 
    'edward': 'rust', 
    'phil': 'python', 
    'pol' : 'python',
    }
print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#El método get() requiere una clave como primer argumento. 
#Como segundo argumento opcional, podemos pasar el valor que se devolverá 
#si la clave no existe:

alien_0 = {'color': 'green', 'speed': 'slow'} 
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


user_0 = { 
    'username': 'efermi', 
    'first': 'enrico',
    'last':'fermi'
    }
for key, value in user_0.items():
    print(f"\nKey: {key}") 
    print(f"Value: {value}")

for name, language in favorite_languages.items(): 
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
for name,code in favorite_languages.items():
    print(code)

friends = ['phil', 'sarah'] 
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.") 
    if name in friends: 
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:") 
for language in favorite_languages.values(): 
    print(language.title())

print("The following languages have been mentioned:") 
for language in sorted(set(favorite_languages.values())): 
    print(language.title())

alien1 = {'color' : 'green' , 'points' : 5,}
alien2 = {'color' : 'yellow' , 'points' : 10,}
alien3 = {'color' : 'red' , 'points' : 15,}

aliens = [alien1,alien2,alien3]

print(aliens)

aliens = [] 
for alines_number in range(30):
    new_alien = {'id' : alines_number , 'color' : 'gree' , 'points' : 5 , 'speed' : 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")

#Hace una lista vacía para guardar aliens. 
aliens = [] 
# Hace 30 aliens verdes. 
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
    aliens.append(new_alien) 
for alien in aliens[:9]: 
    if alien['color'] == 'green': 
        alien['color'] = 'yellow' 
        alien['speed'] = 'medium'
        alien['points'] = 10 
    elif alien['color'] == 'yellow': 
        alien['color'] = 'red' 
        alien['speed'] = 'fast'
        alien['points'] = 15

# Muestra los 5 primeros aliens. 
for alien in aliens[:30]: 
    print(alien)
print("...")



#pizza
# Guarda la información sobre una pizza que se está pidiendo. 
pizza = { 'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }
# Resume el pedido. 
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")
for topping in pizza['toppings']: 
    print(f"\t" + topping.title())


favorite_languages = {
    'jen': ['python', 'rust'], 
    'sarah': ['c'], 
    'edward': ['rust', 'go'], 
    'phil': ['python', 'haskell'], 
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages: 
        print(f"\t{language.title()}")
        
users = { 'aeinstein': { 'first': 'albert',
                        'last': 'einstein',
                        'location': 'princeton',
                        },
         'mcurie': { 'first': 'marie',
                    'last': 'curie',
                    'location': 'paris', }, 
         }

for username, user_info in users.items():
    print(f"\nUsername: {username}") 
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}") 
    print(f"\tLocation: {location.title()}")









