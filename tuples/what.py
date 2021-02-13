'''
   sequence data type 
   create a tuple with ()
   create a tuple using the Tuple() class 

'''

# test_tuple = ()
# print(type(test_tuple))
# print(len(test_tuple))
# print(id(test_tuple))

'''
   Elements within a tuple are ordered 
   Each element is seperated using , 
   Elements can be indexed 
   Elements can be slicied as well ??
'''


# first = ('rahul', 'somani', 24, 45.7, True)
# print(type(first))
# print(first)
# print(first[0])
# print(first[-1])

# print(first[:])
# print(first[1:])

'''
   Immutable ( cannot change )
   we cannot change an item within a tuple 
'''

# second = tuple()
# print(type(second))

# age = (10, 20)
# name = ('rahul', 'somendra')
# result = name + age
# print(result)

example_1 = (10, 20)
example_2 = (40, 50)
nested_tuple = (example_1, example_2)
print(nested_tuple)
print(f' The length is {len(nested_tuple)}')
print(nested_tuple[0][0])
