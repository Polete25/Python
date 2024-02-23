bycicles = ['trek','cannondale','redline','specialized']
print(bycicles)
print(f'\n '+bycicles[1])
print(f'\n '+bycicles[0].title())
print(f'\n My first bike was '+bycicles[-1].title()+f'\n')

bycicles.append('montain')
print(bycicles)

bycicles.insert(1,'trail')
print(bycicles)

del bycicles[1]
print(bycicles)

popped_bycicle = bycicles.pop()
print(bycicles)
print(popped_bycicle)
popped_bycicle1 = bycicles.pop(1)
print(popped_bycicle1)
bycicles.remove('redline')
print(bycicles)
too_expensive = 'trek'
bycicles.remove(too_expensive) # solo borra el primero que encuentra, si queremos borrar más hay que utlizar un bucle
print(bycicles)

cars = ['honda','toyota','bmw','audi','mercedes']
cars.sort()
print(cars)
cars.sort(reverse=True)
print (cars)

cars = ['honda','toyota','bmw','audi','mercedes']
print(f'\nThis is the Original list: ') 
print(cars)
print(f'\nThis is the list shorted by alphabet: ')
print('\n')
print(sorted(cars).reverse())
print('\n')
cars.reverse()
cars.reverse()
print(cars)
print(len(cars))