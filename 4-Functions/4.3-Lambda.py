'''
Lambda Functions in Python:

Lambda functions are small anonymous functions defined using the lambda keyword.
They can have any number of arguments but only one expression. 
They are commonly used for short operations or as arguments to higher-order functions.
'''

## Syntax of lambda functions:
# lambda arguments: expression

# Regular function for addition
def addition(a, b):
    """Regular function to add two numbers"""
    return a + b

print(addition(2, 3))  # 5

# Equivalent lambda function for addition
addition = lambda a, b: a + b
print(type(addition))   # <class 'function'> (shows it's still a function)
print(addition(10, 20))  # 30

# Regular function to check even number
def even(num):
    """Regular function to check if number is even"""
    if num % 2 == 0:
        return True

print(even(30))  # True

# Equivalent lambda function to check even number
even_lambda = lambda x: x % 2 == 0  # Returns True if even, False otherwise
print(even_lambda(11))  # False

# Regular function for three-number addition
def addition(x, y, z):
    """Regular function to add three numbers"""
    return x + y + z

print(addition(12, 13, 14))  # 39

# Equivalent lambda function for three-number addition
addition_lambda = lambda x, y, z: x + y + z
print(addition_lambda(10, 20, 30))  # 60

## Using lambda with map()
# map() applies a function to all items in an iterable (like list)
numbers = [1, 2, 3, 4, 5, 6]

# Regular square function
def square(number):
    """Regular function to square a number"""
    return number ** 2

print(square(9))  # 81

# Using map() with lambda to square all numbers
# Note: map() returns a map object (iterator)
print(map(lambda x: x**2, numbers))          # <map object at 0x7c8bdd9ffaf0>

# Convert map object to list to see results
print(list(map(lambda x: x**2, numbers)))    # [1, 4, 9, 16, 25, 36]