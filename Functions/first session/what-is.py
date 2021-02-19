'''
   Functions
  Syntax :
  def function_name(val1,val2,val3):
    stat1
    stat2
  stat3
  '''

# First Example


# def sayHi():
#     print('Hello, how are you ?')


# def x():
#     print('x')


# def y():
#     print('y')


# def z():
#     print('z')


# print(' The First Function Session')

# z()
# sayHi()

'''
    Passing arguments to a function
'''


def sum(num1, num2):
    print(f'The sum of {num1} and {num2} is {num1+num2}')


# sum(1, 1)
# sum(0, -1)
# sum(-1, 1)
# sum(5, 2)

'''
  Write a function that accepts a list of integers
  and than gives us the sum of all the values in the list 
'''


def sumlist(numbers):
    s = 0
    for item in numbers:
        s = s + item
    # print('The final result is {}'.format(s))
    return(s)


# result = sumlist([1, 2, 3])
# print(result)

# int sum(int a, int b){
#     return a+b
# }


'''
   We can write our functions to behave in a variety of ways 
   1. Default argument function
   2. Variable Number of arguments
   3. Keyword arguments
'''


def printDetails(name, age, gender='Male'):
    print('Hi {} you are {} years {}'.format(name, age, gender))


# printDetails('rahul', 40, 'Male')
# printDetails('rahul', 40)
# printDetails('Somu', 39)
# printDetails('Sush', 39, 'Female')

# Variable number of args example 1

def testVar(*args):
    print(args)
    for i in args:
        print(i)


# testVar(1, 'a', 23.8)

def keyargstest(fruit1, fruit2, fruit3):
    print(fruit1, fruit2, fruit3)


# keyargstest(fruit2='orange', fruit3='apple', fruit1='banana')


def varkeyargs(**kwargs):
    print(kwargs)
    print(*kwargs)
    print(kwargs['lname'])


varkeyargs(fname='rahul', lname='somani')
