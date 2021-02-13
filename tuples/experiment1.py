'''
   Create a tuple , and then delete an item from the tuple
'''

# animals = 'dog', 'cats', 'cow', 'tiger'
# animal_list = list(animals)

# animal_list.remove('cow')

# print(animals, animal_list)
# animal_tuple = tuple(animal_list)
# print('--'*10)
# print(animal_tuple)
# del animal_tuple
# print(animal_tuple)

'''
 Packing and Unpacking 
'''
# vehicles = ('bmw', 'merc', 'lamb')  # packing
# print(vehicles)
# mycar, yourcar, hercar = vehicles  # unpacking
# print(mycar, yourcar, hercar)

age = (10, 20, 30)
_, _, myage = age
print(myage)
print(_)
