'''
  Dictionary is a data structure in python which items 
  every item has a key and a corresposnding value 
  syntax : {key1:value1,key2:value2}
  
  unordered , does not allow duplicate values 
  cannot change ( mutable / immutable )
  
'''

empty_dict = {}
empty_dict_using_class = dict()
print(type(empty_dict))
print(len(empty_dict))

print(type(empty_dict_using_class))
print(len(empty_dict_using_class))
print(id(empty_dict_using_class))


'''
   Adding items 
   deleting items 
   accessing items 
   
'''
phone_book = {"rahul": "8210638822", "somu": "921345678", 'age': 78}
print(len(phone_book))
print(phone_book)
# to access a value , provide the key enclosed within []
print(phone_book["rahul"])
print(phone_book["somu"])  # keys are case sensitive

# duplicates are not allowed, and even if we do so it will update the item based on the key
# accessing value using get() method

result = phone_book.get('somu')
print(result)

# to get keys in the dict
print(phone_book.keys())   # to get keys
print(phone_book.values())  # to get values
print(phone_book.items())  # to get items

if 'som' in phone_book:
    print(' The key is present')
else:
    print(' Not present')


'''
  Changing values 
'''
phone_book['age'] = 79
print(phone_book)

phone_book.update({"somu": "Qatar"})
print(phone_book)

# adding items in dictionary   using update() method

phone_book.update({'gender': 'Male'})
print(phone_book)

phone_book['location'] = '127.0.0.1'
print(phone_book)

# new_phoneBook = {'ujjwal': '9374948'}
# print(new_phoneBook + phone_book)
result = phone_book.pop('gender')
print(result)
print(phone_book)

print(phone_book.popitem())
# print(phone_book.popitem()[1])
# print(phone_book.popitem()[0])

del phone_book['rahul']  # delete based on key
# del phone_book # delete entire dict
# phone_book.clear()  # deletes the content of the dictionary
# print(phone_book)
