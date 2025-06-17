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


print("----------------------")
## Basics Sets Operation
## Adding and Removing Elements
my_set.add(7)
print(my_set)
my_set.add(7)
print(my_set)
'''
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
'''

## Remove the elements from a set
my_set.remove(3)
print(my_set)    # {1, 2, 4, 5, 6, 7}

# my_set.remove(100)
'''
KeyError                                  Traceback (most recent call last)
Cell In[11], line 1
----> 1 my_set.remove(10)

KeyError: 10
'''

my_set.discard(99)
print(my_set)  # {1, 2, 4, 5, 6, 7}

## pop method
removed_element=my_set.pop()
print(removed_element) # 1
print(my_set)          # {2, 4, 5, 6, 7} 

## clear all elements
my_set.clear()
print(my_set)   # set()

## Set Memebership test
my_set={1,2,3,4,5}
print(3 in my_set)      # True
print(10 in my_set)     # False

print("-----------------")
## Mathematical Operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

## Union
union_set=set1.union(set2)
print(union_set)            # {1, 2, 3, 4, 5, 6, 7, 8, 9}

## Intersection
intersection_set=set1.intersection(set2)
print(intersection_set)     # {4, 5, 6}

set1.intersection_update(set2)
print(set1)                 # {4, 5, 6}
# print(set2)


print("----------------")
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

## Difference 
print(set1.difference(set2)) # {1,2,3}
print(set2.difference(set1)) # {8,9,7}  

## Symmetric Difference
print(set1.symmetric_difference(set2)) # {1, 2, 3, 7, 8, 9}

