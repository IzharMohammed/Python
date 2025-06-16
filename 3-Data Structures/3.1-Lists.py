'''
Lists:- 

Lists are ordered, mutable collections of items.
They can contain items of different data types.
'''
list=[]
print(type(list))


names=["izhar","mohammed","unknmown",1,2,3]
print(names)

mixed_lists=[1,"Hello",3.14,True,False]
print(mixed_lists)

### Accessing List elements
fruits=["apple","banana","cherry","kiwi","gauva"]
print(fruits[4])
print(fruits[-1])

print(fruits[2:])
print(fruits[1:3])

print("-----------------")

### Modifying list elements
fruits[4]="mango"
print(fruits)

### List methos
fruits.append("orange") ## Add an item to the end 
print(fruits)

fruits.insert(2,"watermelon")
print(fruits)

fruits.remove("kiwi") ## Removing the 1st occurence
print(fruits)

print("-----------------------")

## Remove and return the last
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)

print(fruits.index("mango"))

print("------------")
fruits.insert(2,"banana")
print(fruits)
print(fruits.count("banana"))

fruits.sort() ## sort the list in ascending order
print(fruits)

fruits.reverse() ## Reverse the list
print(fruits)

fruits.clear() ## Remove all items from th list
print(fruits)

print("--------------")

  ## Slicing List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::2])

'''
[3, 4, 5]
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[1, 3, 5, 7, 9]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 3, 5, 7, 9]
'''

print("-----------------")

### Iterating over lists
for number in numbers:
    print(number)

## iterating with index
for index,number in enumerate(numbers):
    print(index,number)

## List comprehension
lst=[]
for x in range(10):
    lst.append(x**2)
print(lst)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([x**2 for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("-----------")
## List Comprehension
## Basics Syantax             [expression for item in iterable]
## with conditional logic     [expression for item in iterable if condition]
## Nested List Comprehension  [expression for item1 in iterable1 for item2 in iterable2]

##Basic list comprehension

square=[num**2 for num in range(10)]
print(square)

## List compre. with condition
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)
print(lst)

even_numbers=[num for num in range(10) if num%2==0]
print(even_numbers)

## Nested list comprehension
lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2]
print(pair)
## [[1, 'a'], [1, 'b'], [1, 'c'], [1, 'd'], [2, 'a'], [2, 'b'], [2, 'c'], [2, 'd'], [3, 'a'], [3, 'b'], [3, 'c'], [3, 'd'], [4, 'a'], [4, 'b'], [4, 'c'], [4, 'd']]

## List comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
length=[len(word) for word in words]
print(length)
## [5, 5, 6, 4, 13]

'''
Conclusion
List comprehensions are a powerful and concise way to create lists in Python. 
They are syntactically compact and can replace more verbose looping constructs. 
Understanding the syntax of list comprehensions will help you write cleaner and more efficient Python code.
'''