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