'''
The map() Function in Python:-

The map() function applies a given function to all items in an input list (or any other iterable) and
returns a map object (an iterator). This is particularly useful for transforming data in a list comprehensively.
'''

def square(x):
    return x*x

print(square(10)) # 100

numbers=[1,2,3,4,5,6,7,8]
print(list(map(square,numbers)))  # [1, 4, 9, 16, 25, 36, 49, 64]

## Lambda function with map
numbers=[1,2,3,4,5,6,7,8]
print(list(map(lambda x:x*x, numbers))) # [1, 4, 9, 16, 25, 36, 49, 64]

### Map multiple iterables

numbers1=[1,2,3,4,5]
numbers2=[4,5,6,6]
added_numbers=list(map(lambda x,y: x+y, numbers1, numbers2))
print(added_numbers)  # [5, 7, 9,10]

## map() to convert a list of strings to integers
# Use map to convert strings to integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers=list(map(int,str_numbers))
print(int_numbers)  # [1, 2, 3, 4, 5]

words=['apple','banana','cherry']
upper_word=list(map(str.upper,words))
print(upper_word)       # ['APPLE', 'BANANA', 'CHERRY']

def get_name(person):
    return person["name"]

people=[
    {'name':'izhar','age':21},
    {'name':'Jack','age':33}
]

print(list(map(get_name,people))) # ['izhar', 'Jack']