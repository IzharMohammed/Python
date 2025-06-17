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

## Creating Tuples
# Creating an empty tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))
'''
()
<class 'tuple'>
'''

# Creating empty list and tuple
lst=list()
print(type(lst))
tpl=tuple()
print(type(tuple))
'''
<class 'list'>
<class 'tuple'>
'''

# Creating tuple from list
numbers=tuple([1,2,3,4,5,6])
print(numbers) ## (1, 2, 3, 4, 5, 6)

# Creating list from tuple
lst = list((1,2,3,4,5,6,7))
print(lst) ## [1, 2, 3, 4, 5, 6, 7]

# Mixed data type tuple
mixed_tuple=(1,"Hello world",3.14,True)
print(mixed_tuple) ## (1, 'Hello world', 3.14, True)

## Accessing Tuple Elements
# Basic indexing and slicing
print(numbers)        # (1, 2, 3, 4, 5, 6)
print(numbers[3])     # 4 (positive indexing)
print(numbers[-1])    # 6 (negative indexing)
print(numbers[0:4])   # (1, 2, 3, 4) (slicing)
print(numbers[::])    # (1, 2, 3, 4, 5, 6) (full slice)
print(numbers[::-1])  # (6, 5, 4, 3, 2, 1) (reverse)

## Tuple Operations
# Concatenation - combining tuples
concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple) # (1, 2, 3, 4, 5, 6, 1, 'Hello world', 3.14, True)

# Repetition - repeating tuples
print(mixed_tuple*3)       # (1, 'Hello world', 3.14, True, 1, 'Hello world', 3.14, True, 1, 'Hello world', 3.14, True)
print(numbers*3)           # (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

print("---------------------")

## Immutable Nature Of Tuples
# Tuples are immutable, meaning their elements cannot be changed once assigned
lst=[1,2,3,4,5]
print(lst)

# Lists are mutable
lst[1]="izhar"
print(lst)
'''
[1, 2, 3, 4, 5]
[1, 'izhar', 3, 4, 5]
'''

# This would raise an error since tuples are immutable
# numbers[1]="izhar"
'''
    numbers[1]="izhar"
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

## Tuple Methods
# count() - Returns number of occurrences of a value
print(numbers.count(1)) # 1

# index() - Returns first index of a value
print(numbers.index(3)) # 2

## Packing and Unpacking tuple
# Packing - creating tuple without parentheses
packed_tuple=1,"Hello",3.14
print(packed_tuple) # (1, 'Hello', 3.14)

# Unpacking - assigning tuple elements to variables
a,b,c=packed_tuple
print(a) # 1
print(b) # Hello
print(c) # 3.14

# Extended unpacking with * operator
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers

print(first)    # 1
print(middle)   # [2,3,4,5] (middle elements collected in list)
print(last)     # 6

## Nested Tuple
# Nested List example
lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"]]
print(lst[0][1:3]) # [2,3] (slicing nested list)
print(lst[2][1:3]) # ['Hello', 3.14]

# List containing tuple
lst=[[1,2,3,4],[6,7,8,9],(1,"Hello",3.14,"c")]
print(lst[2][0:3]) # (1, 'Hello', 3.14)

# Nested tuple
nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))

# Accessing nested elements
print(nested_tuple[0])      # (1,2,3) (first subtuple)
print(nested_tuple[1][2])   # c (third element of second subtuple)

print("------------------")
## Iterating over nested tuples
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(f"{sub_tuple} : {item}")
    print()

'''
(1, 2, 3) : 1
(1, 2, 3) : 2
(1, 2, 3) : 3

('a', 'b', 'c') : a
('a', 'b', 'c') : b
('a', 'b', 'c') : c

(True, False) : True
(True, False) : False
'''


''''
Conclusion
Tuples are versatile and useful in many real-world scenarios where an immutable and ordered collection of items is required. 
They are commonly used in data structures, function arguments and return values, and as dictionary keys.
Understanding how to leverage tuples effectively can improve the efficiency and readability of your Python code.
'''