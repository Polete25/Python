#current_number = 1 
#while current_number <= 5: 
#    print(current_number) 
#    current_number += 1


#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = "" 
#while message != 'quit':
#    message = input(prompt) 
#    if message != 'quit':
#        print(message)


#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. " 
#active = True 
#while active: 
#    message = input(prompt)
#    if message == 'quit':
#        active = False 
#    else: print(message)


#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.) " 
#while True: 
#    city = input(prompt)
#    if city == 'quit':
#        break 
#    else: 
#        print(f"I'd love to go to {city.title()}!")

#current_number = 0
#while current_number < 10:
#    current_number += 1 
#    if current_number % 2 == 0: 
#        continue 
#    else:
#        print(current_number)
        
        
# Empieza con usuarios que hay que verificar,
# y una lista vacía para alojar a los usuarios confirmados. 

unconfirmed_users = ['alice', 'brian', 'candace'] 
confirmed_users = [] 
# Verifica cada usuario hasta que ya no hay usuarios sin confirmar. 
# Mueve a cada usuario verificado a la lista de usuarios confirmados.

while unconfirmed_users:
    current_user = unconfirmed_users.pop() 
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Muestra todos los usuarios confirmados. 

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users: 
    print(confirmed_user.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets) 
while 'cat' in pets: 
    pets.remove('cat')
print(pets)

responses = {}
 
# Configura una bandera para indicar que la encuesta está activa. 
polling_active = True

while polling_active: 
#Pide el nombre y la respuesta de la persona. 
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Guarda la respuesta en el diccionario.
    responses[name] = response 
# Averigua si alguien más va a hacer la encuesta.
    repeat = input("Alguien más va a hacer la encuesta?")
    if repeat == 'No':
        polling_active = False
        
# La encuesta está completa. Muestra los resultados. 
print("\n--- Poll Results ---") 
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


        
        



