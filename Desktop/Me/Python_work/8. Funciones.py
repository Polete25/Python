def greet_user(): 
    """Muestra un simple saludo.""" 
    print("Hello!") 
greet_user()

greet_user()

def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

def get_formatted_name(first_name, last_name): 
    """Devuelve un nombre completo, con un formato adecuado.""" 
    full_name = f"{first_name} {last_name}" 
    return full_name.title() 
musician = get_formatted_name('jimi', 'hendrix') 
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''): 
    """Devuelve un nombre completo, con un formato adecuado."""
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else: full_name = f"{first_name} {last_name}" 
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician) 
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
    """Devuelve un diccionario de información sobre una persona.""" 
    person = {'first': first_name, 'last': last_name} 
    return person 
musician = build_person('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name):
    """Devuelve un nombre completo, con un formato adecuado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title() 
while True: 
    print("\nPlease tell me your name:") 
    print("(enter 'q' at any time to quit)") 
    f_name = input("First name: ") 
    if f_name == 'q':
        break
    l_name = input("Last name: ") 
    if l_name == 'q': 
        break 
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def greet_users(names):
    """Imprime un saludo sencillo para cada usuario de la lista.""" 
    for name in names: 
        msg = f"Hello, {name.title()}!" 
        print(msg)

usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)

def print_models(unprinted_designs, completed_models):
    """ Simula imprimir cada diseño, hasta que no queda ninguno. Mueve cada
    diseño a completed_models después de la impresión. """
    
    while unprinted_designs:
        current_design = unprinted_designs.pop() 
        print(f"Printing model: {current_design}")
        completed_models.append(current_design) 
def show_completed_models(completed_models):
    print("\nThe following models have been printed:") 
    for completed_model in completed_models: 
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = [] 

print_models(unprinted_designs, completed_models) 
show_completed_models(completed_models)

def make_pizza(*toppings): 
    """Imprime la lista de ingredientes solicitados.""" 
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Resume la pizza que estamos a punto de hacer.""" 
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings:
        print(f"- {topping}") 
        
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """Resume la pizza que estamos a punto de hacer.""" 
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """Crea un diccionario con todo lo que sabemos sobre un usuario.""" 
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    return user_info 

user_profile = build_profile('albert', 'einstein', 
                            location='princeton', 
                            field='physics')
print(user_profile)


