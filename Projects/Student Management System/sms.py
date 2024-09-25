# Step 1: Dictionary to store student data
students = {}


# Step 2: Function to add a new student
def add_student():
    name = input("Enter student's name: ").title()
    age = int(input(f"Enter {name}'s age: "))
    marks = float(input(f"Enter {name}'s marks: "))

    # Add student to the dictionary
    students[name] = {"age": age, "marks": marks}
    print(f"Student {name} added successfully!")


# Step 3: Function to update student marks
def update_marks():
    name = input("Enter the student's name to update marks: ").title()

    if name in students:
        new_marks = float(input(f"Enter new marks for {name}: "))
        students[name]["marks"] = new_marks
        print(f"{name}'s marks updated to {new_marks}!")
    else:
        print(f"Student {name} not found!")


# Step 4: Function to display a student's details
def display_student():
    name = input("Enter the student's name to display details: ").title()

    if name in students:
        print(f"Name: {name}")
        print(f"Age: {students[name]['age']}")
        print(f"Marks: {students[name]['marks']}")
    else:
        print(f"Student {name} not found!")


# Step 5: Function to display all students
def display_all_students():
    if students:
        print("\nAll Students:")
        for name, details in students.items():
            print(f"Name: {name}, Age: {details['age']}, Marks: {details['marks']}")
    else:
        print("No students added yet.")

# Step 8: Main menu
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add a new student")
        print("2. Update student marks")
        print("3. Display a student's details")
        print("4. Display all students")
        # print("5. Find the top student")
        # print("6. Calculate average marks")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            update_marks()
        elif choice == 3:
            display_student()
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Start the Student Management System
menu()
