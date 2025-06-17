''''
Lambda Functions in Python:-

Lambda functions are small anonymous functions defined using the lambda keyword.
They can have any number of arguments but only one expression. 
They are commonly used for short operations or as arguments to higher-order functions.
'''

## syntax
# lambda arguments: expression

def addition(a,b):
    return a+b

print(addition(2,3)) # 5


addition = lambda a,b: a+b
print(type(addition))   # <class 'function'>
print(addition(10,20))  # 30

def even(num):
    if num%2==0:
        return True

print(even(30)) # True

even_lambda = lambda x:x%2==0
print(even_lambda(11)) # False

def addition(x,y,z):
    return x+y+z

print(addition(12,13,14)) # 39

addition_lambda=lambda x,y,z:x+y+z
print(addition_lambda(10,20,30))   # 60

## map()- applies a function to all items in a list
numbers=[1,2,3,4,5,6]

def square(number):
    return number**2
print(square(9)) # 81

print(map(lambda x:x**2, numbers))          # <map object at 0x7c8bdd9ffaf0>
print(list(map(lambda x:x**2, numbers)))    # [1, 4, 9, 16, 25, 36]