'''
Sets
Sets are a built-in data type in Python used to store collections of unique items.
They are unordered, meaning that the elements do not follow a specific order, and
they do not allow duplicate elements. Sets are useful for membership tests, eliminating duplicate entries,
and performing mathematical set operations like union, intersection, difference, and symmetric difference.
'''

## create a set
my_set={1,2,3,4,5,6}
print(my_set)
print(type(my_set))
'''
{1, 2, 3, 4, 5, 6}
<class 'set'>
'''

my_empty_set=set()
print(type(my_empty_set)) # <class 'set'>

my_set=set([1,2,3,4,5,6])
print(my_set) # {1, 2, 3, 4, 5, 6}

## sets remove duplicate entries
my_empty_set=set([1,2,3,6,5,4,5,6,1,2,3,4,5,6,1,2,3,4,5,5,5,2,2])
print(my_empty_set) # {1, 2, 3, 4, 5, 6}




