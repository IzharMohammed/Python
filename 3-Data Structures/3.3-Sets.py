'''
Sets
Sets are a built-in data type in Python used to store collections of unique items.
They are unordered, meaning that the elements do not follow a specific order, and
they do not allow duplicate elements. Sets are useful for membership tests, eliminating duplicate entries,
and performing mathematical set operations like union, intersection, difference, and symmetric difference.
'''

## create a set
# Initializing a set with elements
my_set={1,2,3,4,5,6}
print(my_set)
print(type(my_set))
'''
{1, 2, 3, 4, 5, 6}
<class 'set'>
'''

# Creating an empty set (note: {} creates a dictionary, so we use set())
my_empty_set=set()
print(type(my_empty_set)) # <class 'set'>

# Creating a set from a list
my_set=set([1,2,3,4,5,6])
print(my_set) # {1, 2, 3, 4, 5, 6}

## sets remove duplicate entries
# Automatically removes duplicates when created from a list with duplicates
my_empty_set=set([1,2,3,6,5,4,5,6,1,2,3,4,5,6,1,2,3,4,5,5,5,2,2])
print(my_empty_set) # {1, 2, 3, 4, 5, 6}


print("----------------------")
## Basics Sets Operation
## Adding and Removing Elements
# add() - Adds an element to the set
my_set.add(7)
print(my_set)
# Adding duplicate element (has no effect)
my_set.add(7)
print(my_set)
'''
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
'''

## Remove the elements from a set
# remove() - Removes specified element, raises KeyError if not found
my_set.remove(3)
print(my_set)    # {1, 2, 4, 5, 6, 7}

# my_set.remove(100)
'''
KeyError                                  Traceback (most recent call last)
Cell In[11], line 1
----> 1 my_set.remove(10)

KeyError: 10
'''

# discard() - Removes element if present (no error if not found)
my_set.discard(99)
print(my_set)  # {1, 2, 4, 5, 6, 7}

## pop() - Removes and returns an arbitrary element from the set
removed_element=my_set.pop()
print(removed_element) # 1
print(my_set)          # {2, 4, 5, 6, 7} 

## clear() - Removes all elements from the set
my_set.clear()
print(my_set)   # set()

## Set Membership test
# Using 'in' keyword to check if element exists in set
my_set={1,2,3,4,5}
print(3 in my_set)      # True
print(10 in my_set)     # False

print("-----------------")
## Mathematical Operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

## Union
# union() or | - Returns a new set with elements from both sets
union_set=set1.union(set2)
print(union_set)            # {1, 2, 3, 4, 5, 6, 7, 8, 9}

## Intersection
# intersection() or & - Returns common elements between sets
intersection_set=set1.intersection(set2)
print(intersection_set)     # {4, 5, 6}

# intersection_update() - Updates the set with the intersection
set1.intersection_update(set2)
print(set1)                 # {4, 5, 6}
# print(set2)


print("----------------")
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

## Difference 
# difference() or - - Returns elements in set1 but not in set2
print(set1.difference(set2)) # {1,2,3}
print(set2.difference(set1)) # {8,9,7}  

## Symmetric Difference
# symmetric_difference() or ^ - Returns elements in either set but not both
print(set1.symmetric_difference(set2)) # {1, 2, 3, 7, 8, 9}


print("-----------------")
## sets methods
set1={1,2,3,4,5}
set2={3,4,5}

# issubset() - Checks if all elements of set2 are in set1
print(set2.issubset(set1))   # True

# issuperset() - Checks if set1 contains all elements of set2
print(set1.issuperset(set2)) # True

# Converting list to set to remove duplicates
lst=[1,2,2,3,4,4,5]
print(set(lst)) # {1, 2, 3, 4, 5}


### Counting Unique words in text
text="In this tutorial we are discussing about sets In this tutorial we are discussing about sets"
words=text.split()
print(words)
# ['In', 'this', 'tutorial', 'we', 'are', 'discussing', 'about', 'sets', 'In', 'this', 'tutorial', 'we', 'are', 'discussing', 'about', 'sets']

## convert list of words to set to get unique words
unique_words=set(words)
print(unique_words)         # {'sets', 'discussing', 'we', 'about', 'In', 'this', 'are', 'tutorial'}
print(len(unique_words))    # 8


'''
Conclusion:
Sets are a powerful and flexible data type in Python that provide a way to store collections of unique elements.
They support various operations such as union, intersection, difference, and symmetric difference, which are useful 
for mathematical computations. Understanding how to use sets and their associated methods can help you write more 
efficient and clean Python code, especially when dealing with unique collections and membership tests.
'''