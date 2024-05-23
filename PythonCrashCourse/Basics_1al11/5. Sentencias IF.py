cars = ['audi', 'bmw', 'subaru', 'toyota'] 
for car in cars: 
    if car == 'bmw': 
        print(car.upper())
    else: print(car.title())
    
requested_toppings = ['mushrooms', 'onions', 'pineapple']  

print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)


age = 19 
if age >= 18: 
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn")

age = 12 
if age < 4:
    print("Your admission cost is $0.") 
elif age < 18:
    print("Your admission cost is $25.")
else: 
    print("Your admission cost is $40.")

age = 1 
if age < 4: 
    price = 0 
elif age < 18: 
    price = 25
else: price = 40 
print(f"Your admission cost is ${price}.\n")

if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.") 
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.") 
print("\nFinished making your pizza!")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings: 
    print(f"Adding {requested_topping}.") 
    print("\nFinished making your pizza!")

for requested_topping in requested_toppings: 
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.") 
    else: 
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")

request_toppings = [] 
if request_toppings: 
    for request_topping in request_toppings: 
        print(f"Adding {request_topping}.") 
    print("\nFinished making your pizza!") 
else: 
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
if requested_topping:
    for requested_topping in requested_toppings: 
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.") 
        else: 
            print(f"Sorry, we don't have {requested_topping}.")
    print("\nFinished making your pizza!")

