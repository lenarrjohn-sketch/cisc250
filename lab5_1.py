# =============================================================================
# Student Name: Michael Johnson
# Lab Title: Lab 5
# Date:
# =============================================================================

from lab5_3 import store_task_list, load_task_list
# 1.1 Task
# todo_list = []


# 1.2 Task Create a function to add a task to the list
def add_task(task):
    """Add a task to the todo list."""
    todo_list.append(task)
    # Display
    print(f"Task '{task}' added.")


# 1.3 Task Create a function to display all tasks
def show_tasks():
    """Show all tasks in the todo list."""

 # Check if the list is empty
    if len(todo_list) == 0:
        print("The todo list is empty.")
    else:
        print("Todo List:")

    # Starting at 1
        index = 1
        for task in todo_list:
            print(f"{index}. {task}")
            index += 1


# 1.4 Task Create a function to remove a task 
def remove_task(number):
    """Remove a task from the todo list."""

    try:
        number = int(number)

        if number >= 1 and number <= len(todo_list):
            removed = todo_list.pop(number - 1)
            # Display the removed task
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# 2.1 Task
def run_todo_app():
    """Run the Todo application."""

# 2.2 Task Display a welcome message
    print("Welcome to the Todo App!")
# 2.3 Task
    while True:
        # 2.4 Task Display menu 
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("What would you like to do? Please select a number:")
        
        # 2.4 Task Show all tasks
        if choice == "1":
            show_tasks()
        # 2.5 Task Add a task
        elif choice == "2":
            task = input("Enter a task description: ")

            # Check for blank input
            if task.strip() == "":
                print("Task cannot be blank.")
            else:
                add_task(task)
        # 2.5.2 Task Remove task
        elif choice == "3":

            # Show task list
            show_tasks()

            if len(todo_list) > 0:
                number = input("Enter task number to remove: ")
                remove_task(number)
        # 2.5.3 Task Exit
        elif choice == "4":
            print("Thank you for using the Todo App!")
            break
        # 2.5.4 Task
        else:
            print("Invalid menu option.")

# Load the task list from JSON 
todo_list = load_task_list()

# 2.6 Task
if __name__ == "__main__":
    run_todo_app()
    store_task_list(todo_list)