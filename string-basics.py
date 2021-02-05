# name = "somendra"
# # print(type(name))

# '''             0 1 2 3 4 5 6 7-->
#  Indexing       s o m e n d r a
#                           -3  -2  -1         <--
# '''


# # print(name[0])   # subscript notation
# # print(name[3])   # subscript notation
# # print(name[7])   # subscript notation
# # print(name[-1])   # subscript notation
# # print(name[-3])   # subscript notation

# '''
# String slicing
# name[start:end]
# name[start:end:step]
# '''

# # print(name[0:4])
# # print(name[:4])
# # print(name[:])
# # print(name)

# # print(name[1:4:2])
# # print(name[1:4])
# print(name[0:-3])


# '''
#    getting length of a string
#    use the len() function
# '''

# print(len(name))

# '''
# Commonly used string methods

# '''


# msg = "what is your name"
# print(msg.capitalize())
# msg_cap = msg.upper()
# print(msg_cap)
# msg_cap = msg_cap.lower()
# print(msg_cap)

'''
count number of occurences in a string 

'''

# your_msg = "This is life"
# # print(your_msg.count('i'))
# # print(your_msg.count('i', 1, 6))


# '''
#    if u want to see whether a particular string ends with a suffix
#     endswith()
#     syntax : str.endswith(suffix)
# '''

# test_suffix = your_msg.endswith('a')
# print(test_suffix)

'''
  find() method 
  index() method

'''


# msg = "Qatar"
# print(msg.index('t'))
# print(msg.index('r'))

# msg = "the 2 of the python session "
# print(msg.index('2'))

# print(msg.find('day'))

# msg = 'rahul123'
# msg_1 = 'rahul somani'
# # print(msg.isalnum())
# # print(msg_1.isalnum())

# print(msg.isalpha())
# print('rahul'.isalpha())


# some_val = "10234 ra"
# print(some_val.isdecimal())

# more_val = "123"
# print(more_val.isdigit())

# print('how'.islower())   # true
# print('hOw'.islower())     # false
# print('How'.islower())      # false
# print('How'.isupper())  # false
# print('HOW'.isupper())  # true


print('rahul somani'.istitle())
print('Rahul Somani'.istitle())
