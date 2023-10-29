# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def print_menu():
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Quit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

    try:
        task_number = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def list_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

while True:
    print_menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        list_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
