# In this project, students will create a Student Management System where they can:
#
# - Add new students: Store student details like name, age, and marks in a dictionary.
#
# - Update student marks: Modify the marks for a specific student.
#
# - Display a student's details: Retrieve and display details for a particular student.
#
# - Calculate average marks: Compute the average marks of all students.
#
# - Find the top student: Identify the student with the highest marks.
#
# - Display all students: Print the details of all students in a formatted way.
from pickletools import optimize

stdnt_mangmt = {}


def add_students():
    name = input('Enter students name: ')
    age = int(input(f'Enter {name} age:  '))
    marks = int(input(f'Enter {name} marks: '))
    stdnt_mangmt[name] = {}
    stdnt_mangmt[name]["age"] = age
    stdnt_mangmt[name]["marks"] = marks
    print(f'Student name is {name} with age of {age} having marks {marks} ')



def update_marks():
    name = input('Enter student name to update marks: ')
    if name in stdnt_mangmt:
        new_marks = float(input('Enter new marks: '))
        stdnt_mangmt[name]["marks"] = new_marks
        print(f'{name} is now having marks {new_marks}  ')
    else:
        print(f'{name} not found')




def dis_details():
    name = input('Enter student name to fetch his/her details: ')
    if name in stdnt_mangmt:
        print(f'{name}')
        print(f'{stdnt_mangmt[name]["age"]}')
        print(f'{stdnt_mangmt[name]["marks"]}')
    else:
        print(f'{name} not found')


def all_stdnts():
    if stdnt_mangmt:
        print('Details of all students are: ')
        for name in stdnt_mangmt:
            age = stdnt_mangmt[name]['age']
            marks = stdnt_mangmt[name]['marks']
            print(f'Name : {name}\nAge : {age}\nMarks : {marks}')
    else:
        print('Student not found')



def menu():
    while True:
        print('a. Add a new student.')
        print('b: Update marks.')
        print("c: Display student's details.")
        print('d: Display all students')
        print('e: Exit From System.')
        option = input('Choose the option:')

        if option == 'a':
            add_students()
        elif option == 'b':
            update_marks()
        elif option == 'c':
            dis_details()
        elif option == 'd':
            all_stdnts()
        elif option == 'e':
            print('Exit')
            break
        else:
            print('Invalid Data')


menu()