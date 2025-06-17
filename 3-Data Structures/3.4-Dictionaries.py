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

print("----------------------")
## Dictionary methods

keys=student.keys() ##get all the keys
print(keys)
values=student.values() ##get all values
print(values)

items=student.items() ##get all key value pairs
print(items)
'''
dict_keys(['name', 'age', 'address'])
dict_values(['izhar', 99, 'India'])
dict_items([('name', 'izhar'), ('age', 99), ('address', 'India')])
'''

## shallow copy
student_copy=student
print(student)
print(student_copy)
'''
{'name': 'izhar', 'age': 99, 'address': 'India'}
{'name': 'izhar', 'age': 99, 'address': 'India'}
'''

student["name"]="md"
print(student)
print(student_copy)
'''
{'name': 'md', 'age': 99, 'address': 'India'}
{'name': 'md', 'age': 99, 'address': 'India'}
'''

print("----------------")
student_copy1=student.copy() ## shallow copy
print(student_copy1)
print(student)
'''
{'name': 'md', 'age': 99, 'address': 'India'}
{'name': 'md', 'age': 99, 'address': 'India'}
'''

student["name"] = "Mohammed izhar updated"
print(student)
print(student_copy1)
'''
{'name': 'Mohammed izhar updated', 'age': 99, 'address': 'India'}
{'name': 'md', 'age': 99, 'address': 'India'}
'''


### Iterating Over Dictionaries
## You can use loops to iterate over dictionatries, keys,values,or items

## Iterating over keys
for keys in student.keys():
    print(keys)
'''
name
age
address
'''


## Iterate over values
for value in student.values():
    print(value)
'''
Mohammed izhar updated
99
India
'''

## Iterate over key value pairs
for key,value in student.items():
    print(f"{key} : {value}")
'''
name : Mohammed izhar updated
age : 99
address : India
'''

print("-----------------------")
## Nested Disctionaries
students={
    "student1":{"name":"izhar","age":32},
    "student2":{"name":"mohammed","age":35}
}
print(students) # {'student1': {'name': 'izhar', 'age': 32}, 'student2': {'name': 'mohammed', 'age': 35}}

## Access nested dictionaries elementss
print(students["student1"]["name"])  # izhar
print(students["student2"]["age"])   # 35

print(students.items())
# dict_items([('student1', {'name': 'izhar', 'age': 32}), ('student2', {'name': 'mohammed', 'age': 35})])

## Iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id} : {student_info}")
    for key,value in student_info.items():
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

## Dictionary comprehension
squares ={x:x**2 for x in range(10)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

## Condition dictionary comprehension
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

## Practical Examples

## Use a dictionary to count the frequency of elements in list
numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1

print(frequency) # {1: 1, 2: 2, 3: 3, 4: 4}

## Merge 2 dictionaries into one

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)  # {'a': 1, 'b': 3, 'c': 4}




'''
Conclusion:
Dictionaries are powerful tools in Python for managing key-value pairs.
They are used in a variety of real-world scenarios, such as counting word frequency, grouping data,
storing configuration settings, managing phonebooks, tracking inventory, and caching results.
 Understanding how to leverage dictionaries effectively can greatly enhance the efficiency and readability of your code.
'''