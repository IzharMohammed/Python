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

# Example without function
num = 24
if num % 2 == 0:
    print("even")
else:
    print("odd")

# Defining a simple function
def even_or_odd(num):
    """This function finds even or odd"""
    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

## Calling the function
even_or_odd(24)

## Function with multiple parameters and return value
def add(a, b):
    """Adds two numbers and returns the result"""
    return a + b

result = add(2, 4)
print(result)

## Default Parameters
# Function with required parameter
def greet(name):
    """Greets a person by name"""
    print(f"Hello {name} Welcome To the paradise")

greet("izhar")

# Function with default parameter value
def greet(name="Guest"):
    """Greets a person by name, defaults to 'Guest'"""
    print(f"Hello {name} Welcome To the paradise")

greet()  # Uses default value
greet("izhar")  # Overrides default value
'''
Hello Guest Welcome To the paradise
Hello izhar Welcome To the paradise
'''

### Variable Length Arguments
## *args - Accepts any number of positional arguments

# Using arbitrary argument name (izhar in this case)
def print_numbers(*izhar):
    """Prints all provided arguments"""
    for number in izhar:
        print(number)

print_numbers(1, 2, 3, 4, 5, 6, 7, 8, "izhar")

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

# Convention is to use *args for variable positional arguments
def print_numbers(*args):
    """Prints all provided positional arguments"""
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5, 6, 7, 8, "izhar")     
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
### **kwargs - Accepts any number of keyword arguments

def print_details(*args, **kwargs):
    """
    Prints both positional and keyword arguments
    *args collects positional arguments as tuple
    **kwargs collects keyword arguments as dictionary
    """
    for val in args:
        print(f"positional argument: {val}")
    for key, val in kwargs.items():
        print(f"{key} : {val}")

print_details(1, 2, 3, 4, "izhar", name="izhar", age="21", country="India")
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
# Function returning a single value
def multiply(a, b):
    """Multiplies two numbers and returns the result"""
    return a * b

print(multiply(2, 3))  # 6

### Returning multiple values (as a tuple)
def multiply(a, b):
    """Returns the product and both input numbers"""
    return a * b, a, b

print(multiply(2, 3))  # (6, 2, 3)