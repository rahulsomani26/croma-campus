'''
   Ask the user for his number and then append it to a list 
   Finally, print all the contents within the list ( phone numbers )
# '''
# phoneBook = []
# phoneNumber = input(' Enter your number ')
# phoneBook.append(phoneNumber)
# print(phoneBook)


ans = True
phoneBook = []
while ans:
    phoneNumber = input(' Enter a number . Press q to quit ')
    if phoneNumber == 'q':
        print(' Exiting the system')
        break
    else:
        phoneBook.append(phoneNumber)
print(phoneBook)
