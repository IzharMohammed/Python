'''
Introduction to Tuples
Creating Tuples
Accessing Tuple Elements
Tuple Operations
Immutable Nature of Tuples
Tuple Methods
Packing and Unpacking Tuples
Nested Tuples
Practical Examples and Common Errors
'''

'''

Introduction to Tuples
Explanation:

Tuples are ordered collections of items that are immutable.
 They are similar to lists, but their immutability makes them different.
'''

## creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

'''
()
<class 'tuple'>
'''

lst=list()
print(type(lst))
tpl=tuple()
print(type(tuple))
'''
<class 'list'>
<class 'tuple'>
'''

numbers=tuple([1,2,3,4,5,6])
print(numbers) ## (1, 2, 3, 4, 5, 6)

lst = list((1,2,3,4,5,6,7))
print(lst) ## [1, 2, 3, 4, 5, 6, 7]

mixed_tuple=(1,"Hello world",3.14,True)
print(mixed_tuple) ## (1, 'Hello world', 3.14, True)

## Accessing tuple elements
print(numbers)        # (1, 2, 3, 4, 5, 6)
print(numbers[3])     # 4
print(numbers[-1])    # 6
print(numbers[0:4])   # (1, 2, 3, 4)
print(numbers[::])    # (1, 2, 3, 4, 5, 6)
print(numbers[::-1])  #(6, 5, 4, 3, 2, 1)

##Tuple operations
concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple) # (1, 2, 3, 4, 5, 6, 1, 'Hello world', 3.14, True)
print(mixed_tuple*3)       # (1, 'Hello world', 3.14, True, 1, 'Hello world', 3.14, True, 1, 'Hello world', 3.14, True)
print(numbers*3)           # (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

print("---------------------")

## Immutable Nature Of Tuples
## Tuples are immutable, meaning their elements cannot be changed once assigned.
lst=[1,2,3,4,5]
print(lst)

lst[1]="izhar"
print(lst)
'''
[1, 2, 3, 4, 5]
[1, 'izhar', 3, 4, 5]
'''

numbers[1]="izhar"
'''
    numbers[1]="izhar"
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''


