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

## Creating Dictionaries
# Empty dictionary using {}
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# Empty dictionary using dict() constructor
empty_dict = dict()
print(empty_dict)        # {}

# Dictionary with initial key-value pairs
student = {"name": "izhar", "age": 32, "grade": 24}
print(student)        # {'name': 'izhar', 'age': 32, 'grade': 24}  
print(type(student))  # <class 'dict'>

# Note: Duplicate keys will overwrite previous values
student = {"name": "izhar", "age": 32, "name": 24}
print(student)  # {'name': 24, 'age': 32}

## Accessing Dictionary Elements
student = {"name": "izhar", "age": 32, "grade": 'A'}
print(student)      # {'name': 'izhar', 'age': 32, 'grade': 'A'}

print("----------------------")
## Accessing elements
# Using square bracket notation
print(student['grade']) # A
print(student['age'])   # 32

# Using get() method - safer as it returns None for missing keys
print(student.get('grade'))       # A
print(student.get('last_name'))   # None  
print(student.get('last_name', "Not Available")) # Not Available

## Modifying Dictionary Elements
# Dictionaries are mutable - can add, update or delete elements
print(student) # {'name': 'izhar', 'age': 32, 'grade': 'A'}

# Updating existing key
student["age"] = 99             
print(student)                # {'name': 'izhar', 'age': 99, 'grade': 'A'}

# Adding new key-value pair
student["address"] = "India"    
print(student)                # {'name': 'izhar', 'age': 99, 'grade': 'A', 'address': 'India'}

# Deleting a key-value pair
del student["grade"]
print(student)                 # {'name': 'izhar', 'age': 99, 'address': 'India'}

print("----------------------")
## Dictionary Methods

# keys() - returns view of all keys
keys = student.keys()
print(keys)

# values() - returns view of all values
values = student.values()
print(values)

# items() - returns view of all key-value pairs
items = student.items()
print(items)
'''
dict_keys(['name', 'age', 'address'])
dict_values(['izhar', 99, 'India'])
dict_items([('name', 'izhar'), ('age', 99), ('address', 'India')])
'''

## Copying Dictionaries
# Shallow copy by reference
student_copy = student
print(student)
print(student_copy)
'''
{'name': 'izhar', 'age': 99, 'address': 'India'}
{'name': 'izhar', 'age': 99, 'address': 'India'}
'''

# Changes affect both references
student["name"] = "md"
print(student)
print(student_copy)
'''
{'name': 'md', 'age': 99, 'address': 'India'}
{'name': 'md', 'age': 99, 'address': 'India'}
'''

print("----------------")
# copy() - creates a shallow copy (new object)
student_copy1 = student.copy()
print(student_copy1)
print(student)
'''
{'name': 'md', 'age': 99, 'address': 'India'}
{'name': 'md', 'age': 99, 'address': 'India'}
'''

# Changes to original don't affect the copy
student["name"] = "Mohammed izhar updated"
print(student)
print(student_copy1)
'''
{'name': 'Mohammed izhar updated', 'age': 99, 'address': 'India'}
{'name': 'md', 'age': 99, 'address': 'India'}
'''

### Iterating Over Dictionaries
# Iterating over keys
for key in student.keys():
    print(key)
'''
name
age
address
'''

# Iterating over values
for value in student.values():
    print(value)
'''
Mohammed izhar updated
99
India
'''

# Iterating over key-value pairs
for key, value in student.items():
    print(f"{key} : {value}")
'''
name : Mohammed izhar updated
age : 99
address : India
'''

print("-----------------------")
## Nested Dictionaries
students = {
    "student1": {"name": "izhar", "age": 32},
    "student2": {"name": "mohammed", "age": 35}
}
print(students) # {'student1': {'name': 'izhar', 'age': 32}, 'student2': {'name': 'mohammed', 'age': 35}}

# Accessing nested elements
print(students["student1"]["name"])  # izhar
print(students["student2"]["age"])   # 35

print(students.items())
# dict_items([('student1', {'name': 'izhar', 'age': 32}), ('student2', {'name': 'mohammed', 'age': 35})])

# Iterating over nested dictionaries
for student_id, student_info in students.items():
    print(f"{student_id} : {student_info}")
    for key, value in student_info.items():
        print(f"{key} : {value}")
'''
student1 : {'name': 'izhar', 'age': 32}
name : izhar
age : 32
student2 : {'name': 'mohammed', 'age': 35}
name : mohammed
age : 35
'''

print("-----------------------")

## Dictionary Comprehension
# Create dictionary with squares
squares = {x: x**2 for x in range(10)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Conditional dictionary comprehension
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

## Practical Examples

# Count frequency of elements in list
numbers = [1,2,2,3,3,3,4,4,4,4]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency) # {1: 1, 2: 2, 3: 3, 4: 4}

# Merge two dictionaries (later values overwrite)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # {'a': 1, 'b': 3, 'c': 4}



'''
Conclusion:
Dictionaries are powerful tools in Python for managing key-value pairs.
They are used in a variety of real-world scenarios, such as counting word frequency, grouping data,
storing configuration settings, managing phonebooks, tracking inventory, and caching results.
 Understanding how to leverage dictionaries effectively can greatly enhance the efficiency and readability of your code.
'''