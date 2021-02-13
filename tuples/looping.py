# '''
#   Navigate through each element of the tuple
#   using for statement
# '''

# books = ('automate the boring stuff',
#          'wierd ways', '10 ways to be successfull')
# for item in books:
#     print(f' Your are currently reading "{item}"')

# index = 0
# while index < len(books):
#     print(books[index])
#     index = index + 1
# print('-----'*10)
# print(books*2)


# count the number of times 10 occurs ( with and without using count() method)
# numbers = (10, 20, 10, 10, 1, 2, 10, 3, 10)
numbers = (1, 2, 3, 4)
print(numbers.count(10))
index = 0
counter = 0
while index < len(numbers):
    if numbers[index] == 10:   # == equality operator
        counter = counter + 1

    # print(numbers[index])
    index = index + 1
print(f' you occured {counter} times')

print(numbers.index(3))
