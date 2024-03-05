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


