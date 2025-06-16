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




