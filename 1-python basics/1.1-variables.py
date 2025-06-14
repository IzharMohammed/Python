a=1000
print(a)

## Declaring and assigning variables
height=6.2
name="izhar"
is_student=True

print(height)
print(name)
print(is_student)

## Naming Conventions",
    ## Variable names should be descriptive,
    ## They must start with a letter or an '_' and contains letter,numbers and underscores",
    ## variables names case sensitive

## valid variable names
first_name="izhar"
last_name="MD"

## invalid variable names
##first-name="i"
##@name="i"

## case sensitivity
name="izhar"
Name="izhar"

## understanding variable types 
## Python is dynamically typed,type of a variable is determined at runtime

## Type conversion
age=32
print(type(age))

age_str=str(age)
print(age_str)
print(type(age_str))

age="32"
print(type(int(age)))

## Invalid conversion
name="izhar"
# print(int(name))

## Dynamic typing
## python allows the type of a variable to change as program executes
var=10
print(var,type(var))

var="izhar"
print(var,type(var))

age=int(input("what is the age "))
print("age is :",age)


## simple calculator

first = int(input("Enter 1st value "))
second = int(input("Enter 2nd value "))

sum = first+ second
diff = first-second
mul = first*second
div = first/second

print("Sum is :",sum)
print("diff is :",diff)
print("Mul is :",mul)
print("div is :",div)