'''
Functions in Python

Introduction to Functions
Defining Functions
Calling Functions
Function Parameters
Default Parameters
Variable-Length Arguments
Return Statement
'''

## Introduction to Functions
## Definition:

## A function is a block of code that performs a specific task. Functions help in organizing code, reusing code, and improving readability.


num=24
if num%2==0:
    print("even")
else:
    print("odd")

def even_or_odd(num):
    """This function finds even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")


## Call this function
even_or_odd(24)


## function with multiple parameters

def add(a,b):
    return a+b

result=add(2,4)
print(result)

## Default Parameters

def greet(name):
    print(f"Hello {name} Welcome To the paradise")

greet("izhar")

def greet(name="Guest"):
    print(f"Hello {name} Welcome To the paradise")

greet()
greet("izhar")
'''
Hello Guest Welcome To the paradise
Hello izhar Welcome To the paradise
'''

### Variable Length Arguments
## Positional And Keywords arguments

def print_numbers(*izhar):
    for number in izhar:
        print(number)

print_numbers(1,2,3,4,5,6,7,8,"izhar")
'''
1
2
3
4
5
6
7
8
izhar
'''

## Positional arguments
def print_numbers(*args):
    for number in args:
        print(number)


print_numbers(1,2,3,4,5,6,7,8,"izhar")     
'''
1
2
3
4
5
6
7
8
izhar
'''

print("-----------------")
### Keywords Arguments

def print_details(*args,**kwargs):
    for val in args:
        print(f"positional argument: {val}")
    for key,val in kwargs.items():
        print(f"{key} : {val}")

print_details(1,2,3,4,"izhar",name="izhar",age="21",country="India")

'''
positional argument: 1
positional argument: 2
positional argument: 3
positional argument: 4
positional argument: izhar
name : izhar
age : 21
country : India
'''

### Return statements
def multiply(a,b):
    return a*b

print(multiply(2,3))  # 6

### Return multiple parameters
def multiply(a,b):
    return a*b , a , b

print(multiply(2,3)) # (6, 2, 3)