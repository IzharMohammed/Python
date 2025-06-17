'''
The map() Function in Python:

The map() function applies a given function to all items in an input list (or any other iterable) and
returns a map object (an iterator). This is particularly useful for transforming data in a list comprehensively.
'''

# Regular function to square a number
def square(x):
    """Returns the square of a number"""
    return x * x

print(square(10))  # 100

# Using map() with a regular function
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(square, numbers)))  # [1, 4, 9, 16, 25, 36, 49, 64]

## Lambda function with map()
# Often used for simple transformations where creating a separate function isn't necessary
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(lambda x: x * x, numbers)))  # [1, 4, 9, 16, 25, 36, 49, 64]

### Map with multiple iterables
# map() can accept multiple iterables and apply a function to corresponding items

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [4, 5, 6, 6]
added_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added_numbers)  # [5, 7, 9, 10] 
# Note: Stops at the shortest iterable (5th element of numbers1 is ignored)

## Type conversion with map()
# Useful for converting elements in a list to another type

# Convert strings to integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))
print(int_numbers)  # [1, 2, 3, 4, 5]

# Convert strings to uppercase
words = ['apple', 'banana', 'cherry']
upper_word = list(map(str.upper, words))
print(upper_word)  # ['APPLE', 'BANANA', 'CHERRY']

## Extracting specific values from dictionaries
# Useful for processing collections of dictionaries

def get_name(person):
    """Extracts the 'name' value from a person dictionary"""
    return person["name"]

people = [
    {'name': 'izhar', 'age': 21},
    {'name': 'Jack', 'age': 33}
]

print(list(map(get_name, people)))  # ['izhar', 'Jack']

# Equivalent using lambda:
print(list(map(lambda p: p["name"], people)))  # ['izhar', 'Jack']


'''

Conclusion:-

The map() function is a powerful tool for applying transformations to iterable data structures.
It can be used with regular functions, lambda functions, and even multiple iterables, providing a 
versatile approach to data processing in Python. By understanding and utilizing map(), you can write 
more efficient and readable code.
'''