'''
Introduction to Dictionaries
Creating Dictionaries
Accessing Dictionary Elements
Modifying Dictionary Elements
Dictionary Methods
Iterating Over Dictionaries
Nested Dictionaries
Dictionary Comprehensions
Practical Examples and Common Errors
'''

'''
Introduction to Dictionaries
Dictionaries are unordered collections of items. They store data in key-value pairs.
Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any type.
'''

## creating dictionares
empty_dict={}
print(type(empty_dict))  # <class 'dict'>

empty_dict=dict()
print(empty_dict)        # {}

student={"name":"izhar","age":32,"grade":24}
print(student)        # {'name': 'izhar', 'age': 32, 'grade': 24}  
print(type(student))  # <class 'dict'>

# Single key is slways used
student={"name":"izhar","age":32,"name":24}
print(student)  # {'name': 24, 'age': 32}

## accessing Dictionary Elements
student={"name":"izhar","age":32,"grade":'A'}
print(student)      # {'name': 'izhar', 'age': 32, 'grade': 'A'}

print("----------------------")
## Accessing Dictionary elements
print(student['grade']) # A
print(student['age'])   # 32

## Accessing using get() method
print(student.get('grade'))       # A
print(student.get('last_name'))   # None  
print(student.get('last_name',"Not Available")) # Not Available

## Modifying Dicitonary Elements
## Dictionary are mutable,so you can add, update or delete elements
print(student) # {'name': 'izhar', 'age': 32, 'grade': 'A'}

student["age"]=99             ##update value for the key
print(student)                # {'name': 'izhar', 'age': 99, 'grade': 'A'}
student["address"]="India"    ## added a new key and value
print(student)                # {'name': 'izhar', 'age': 99, 'grade': 'A', 'address': 'India'}

del student["grade"]
print(student)                 # {'name': 'izhar', 'age': 99, 'address': 'India'}



