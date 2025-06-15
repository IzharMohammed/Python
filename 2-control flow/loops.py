print(range(5))

for i in range(5):
    print(i)
print("---------------------")

for i in range(2,7):
    print(i)
print("---------------------")

for i in range(0,10,2):
    print(i)
print("---------------------")

for i in range(10,1,-1):
    print(i)
print("---------------------")

## strings 
str="Mohammed izhar"
for i in str:
    print(i)
print("---------------------")


## while loop
count=0
while count<5:
    print(count)
    count+=1
print("---------------------")

## Loop Control Statements

## break
## The break statement exits the loop permaturely

## break sstatement

for i in range(10):
    if(i==5):
        break
    print(i)
print("---------------------")

## continue

## The continue statement skips the current iteration and continues with the next.
for i in range(10):
    if i%2==0:
        continue
    print(i)
print("---------------------")

## pass
## The pass statement is a null operation; it does nothing.
for i in range(5):
    if i==3:
        pass
    print(i)
print("---------------------")

## Nested loopss
## a loop inside a loop

for i in range(5):
    for j in range(3):
        print(f"i: {i} and j: {j}")
print("---------------------")

## Examples- Calculate the sum of first N natural numbers using a while and for loop

## while loop  

n = int(input("enter a number: "))
result = 0
while n>0:
    result=result+n
    n-=1
print(f"Sum of {n} natural numbers in while loop is: {result}")
print("---------------------")

## for loop
n = int(input("enter a number: "))
result1=0
print(f"n: {n}")
for i in range(n+1):
    print(i)
    result1=result1+i
print(f"Sum of {n} natural numbers in for loop is {result1}")


#Conclusion:
#Loops are powerful constructs in Python that allow you to execute a block of code multiple times. 
# By understanding and using for and while loops, along with loop control statements like break, continue, and pass,
#  you can handle a wide range of programming tasks efficiently.