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

student={"name":"Krish","age":32,"grade":24}
print(student)        # {'name': 'Krish', 'age': 32, 'grade': 24}  
print(type(student))  # <class 'dict'>

# Single key is slways used
student={"name":"Krish","age":32,"name":24}
print(student)  # {'name': 24, 'age': 32}







