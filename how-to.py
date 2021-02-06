# '''
#   1. List is a data structure
#   2. It can store multiple values of different types seperated by comma
#   3. It is mutable in nature  ( Can be changed )
#   4. It is a very versatile data strucure

#   To create a list use the square brackets []
#   name = []   ----=> Empty List
#   name = List()

# '''

# # list_0 = []
# # print(len(list_0))
# # print(type(list_0))
# # print(id(list_0))


# # list_1 = [1, 2, 3, 4]
# # print(len(list_1))
# # print(type(list_1))
# # print(list_1)
# # print(id(list_1))

# # list_2 = ['somu', 34, 'aviation industry', 'qatar', 123.789, True]
# # print(list_2[1])  # positive indexing
# # print(list_2[-1])  # negative indexing

# # '''
# # '''
# # print(list_2[0:4])  # Slicing
# # print(list_2[2:-2])  # Slicing

# '''
#  adding two or more lists
# '''
# # list_add = ['married']
# # print(list_add+list_2)
# listz = ['rahul', ['trainer', '12 years experience'], [40, 'bihar']]
# # print(listz[0])
# # print(listz[1])
# # print(listz[2])

# # print(listz[1][0])
# # print(listz[2][1])

# '''
#    Methods on Lists ( Not a comprehensive )

#    1 . append()
#    2 . extend()
#    3 . count()
#    4 . insert()
#    5 . pop()
#    6.  del statement


# '''

# my_list = []
# my_list.append(1)
# # print(my_list)
# my_list.append(23)
# # print(my_list)
# my_list.append('My Name ')
# my_list.append([23.9])
# print(my_list)

# my_list.extend([4, 6, 7, 8, 9])
# print(my_list)


# my_list.insert(2, 'somu')

# print('--'*20)
# print(my_list)

# '''
#    deleting one item at a time

#    pop() method

# # '''
# # print(my_list.pop())
# # print(my_list)

# del my_list[0]   # delete a particular item within a list
# print(my_list)

# del my_list
# print(my_list)

# ''


my_list = [1, 2, 3, 2, 2, 3, 2, 1, 2]
print(f' The number of times item 1 occured is {my_list.count(1)}')
print(f' The number of times 2 occured is {my_list.count(2)}')
print(f' The number of times 3 occured is {my_list.count(3)}')
print(my_list.count(9))
