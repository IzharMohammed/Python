## Example 1. Manage A To Do List
## Create a To Do List To Keep Track OF Tasks

todo_item=str(input("Enter a list of item: "))
todo_list=[]
index=1

todo_list.append(todo_item)
print(todo_list)

times = int(input("Enter how many items r there: "))

for i in range(times):
    todo_item=str(input("Enter a list of item: "))
    todo_list.insert(index,todo_item)
    index+=1

print(todo_list)

is_modifying=str(input("Do u want to modify any element (y/n): "))

if(is_modifying=="y"):
    is_modify_index=int(input("Enter a index u want to modidy: "))
    todo_list.insert(is_modify_index,str(input("Enter a item u want to modify: ")))
    print(todo_list)    

is_delete=str(input("Do u want to delete a element (y/n): "))

if(is_delete=="y"):
    is_delete_element=str(input("Enter a element u want to delete"))
    todo_list.remove(is_delete_element)
    print(todo_list)


## Example 2: Organizing Student Grades
## Create a list to store and calculate average grades for students

ran = int(input('Enter no of students r present: '))
grades_list=[]
for i in range(ran):
    grades = int(input("Enter grades of students: "))
    grades_list.insert(i,grades)

print(grades_list)
average_grade=sum(grades_list)/len(grades_list)

print(f"avg is: {average_grade}")
print(f"highest is: {max(grades_list)}")
print(f"lowest is: {min(grades_list)}")

