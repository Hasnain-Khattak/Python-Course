def display_menu():
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Remove a task")
    print("5. Exit")


def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + "\n")



def add_task(tasks):
    new_task = input("Enter the new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            print()



def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the number of the task to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_number] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number!")



def remove_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number!")



def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the to-do list app.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()

