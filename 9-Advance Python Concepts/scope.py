# Global variable 'username' is defined outside any function
username = "izhar"

def func():
    # username = "chai"
    print(username)  # This prints the global 'username' ("izhar") since no local variable exists

func()  # Output: "izhar"

# Global variable 'x' is initialized
x = 99

def func2(y):
    # 'x' is accessed from the global scope
    z = x + y  # Uses global x (99) + parameter y (1)
    return z

result = func2(1)  # 99 + 1 = 100
print(result)  # Output: 100

def func3():
    global x  # This declares we're modifying the global 'x'
    x = 12  # Changes the global x to 12

func3()
print(x)  # Output: 12 (global x was modified)

# Example of a closure (function that remembers values in enclosing scope)
def f1():
    x = 88  # Local variable to f1
    
    def f2():
        print(x)  # Remembers x from enclosing scope (88)
    
    return f2  # Returns the inner function (closure)

myResult = f1()  # myResult now contains the f2 function

print(type(myResult))  # Output: <class 'function'>
myResult()  # Output: 88 (executes f2 which remembers x=88)

# Another closure example (function factory)
def chaicoder(num):
    def actual(x):
        return x ** num  # 'num' is remembered from outer function
    return actual

f = chaicoder(2)  # Creates a squaring function (x^2)
g = chaicoder(3)  # Creates a cubing function (x^3)

print(f(3))  # Output: 9 (3^2)
print(g(3))  # Output: 27 (3^3)