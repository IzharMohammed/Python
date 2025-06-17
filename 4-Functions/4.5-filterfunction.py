'''
The filter() Function in Python:

The filter() function constructs an iterator from elements of an iterable for which a function returns true.
It is used to filter out items from a list (or any other iterable) based on a condition.
'''

# Regular function to check if a number is even
def even(num):
    """Returns True if number is even, None otherwise"""
    if num % 2 == 0:
        return True

print(even(10))  # True

# Comparing map() and filter() behavior
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# map() applies the function to all elements
print(list(map(even, lst)))
# [None, True, None, True, None, True, None, True, None, True, None, True]

# filter() only keeps elements where function returns True
print(list(filter(even, lst)))
# [2, 4, 6, 8, 10, 12]

## filter() with Lambda Functions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter numbers greater than 5 using lambda
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # [6, 7, 8, 9]

## Multiple Conditions in filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Filter numbers that are both even AND greater than 5
even_and_greater_than_five = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(even_and_greater_than_five)  # [6, 8, 10, 12, 14, 16, 18, 20]

## Filtering Dictionaries

people = [
    {'name': 'izhar', 'age': 21},
    {'name': 'Jack', 'age': 33},
    {'name': 'John', 'age': 25}
]

# Function to filter people older than 25
def age_greater_than_25(person):
    """Returns True if person's age is greater than 25"""
    return person["age"] > 25

# Filter the list of dictionaries
print(list(filter(age_greater_than_25, people)))
# [{'name': 'Jack', 'age': 33}]

# Equivalent using lambda:
print(list(filter(lambda p: p["age"] > 25, people)))
# [{'name': 'Jack', 'age': 33}]





'''
Conclusion:-
The filter() function is a powerful tool for creating iterators that filter items out of an iterable based on a 
function. It is commonly used for data cleaning, filtering objects, and removing unwanted elements from lists. 
By mastering filter(), you can write more concise and efficient code for processing and manipulating collections in Python.
'''