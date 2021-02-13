
'''
  Looping through the dictionary 
  for statement
'''


addressBook = {'Me': 'Patna, India', 'Your': 'Qatar , Doha'}
for key in addressBook:
    print(addressBook[key])

for key in addressBook.values():
    print(key)
print('-'*10)
for key in addressBook.keys():
    print(key)


name, address = addressBook.items()
print(name, address)


for name, _ in addressBook.items():
    print(name, _)


test = {

    'description1': {
        'age': 40,
        'gender': 'male'
    },

    'description2': {
        'age': 20,
        'gender': 'male',
        'name': 'Ali'
    },
}
print(test['description1'])
