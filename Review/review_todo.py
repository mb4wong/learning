# TASK: To-Do List: Build a command-line to-do list manager where you can add tasks, mark them as completed, and remove them.
# FUNCTIONALITY:
# - Runs in its own terminal window
# - Tasks can either be incomplete; completed; or removed.
# - Incomplete tasks have been added by user but not marked complete or removed. They are typically displayed.
# - Completed tasks are ones that are marked complete by the user but not deleted. They remain in-app, but are not displayed unless requested.
# - Removed tasks are ones that the user marks for deletion. They are deleted from memory. Users are prompted if they are sure they want them to be deleted.
# - BONUS TASK 1: USER/LOG-IN BASED TASKS THINGS
# - BONUS TASK 2: SIMPLIFY UI WITHOUT NEED FOR NUMBERS

task_list = []
completed_task_list = []

def add_task(task):
    task_list.append(task)

def remove_task(task_number):
    if 1 <= task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

def complete_task(task_number):
    if 1 <= task_number <= len(task_list):
        completed_task = task_list[task_number - 1]
        completed_task_list.append(completed_task)
        task_list.pop(task_number - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task nummber> Please enter a valid task number.")

def display_incomplete_tasks():
    if not task_list:
        print("No incomplete tasks!")
    else:
        print("Incomplete Tasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

def display_completed_tasks():
    if not completed_task_list:
        print("No tasks!")
    else:
        print("Completed Tasks:")
        for i, task in enumerate(completed_task_list, 1):
            print(f"{i}. {task}")

def todolist():
    while True:
        print("\n\nOptions: ")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Display Incomplete Tasks")
        print("5. Display Completed Tasks")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            display_incomplete_tasks()
            task_number = int(input("Enter the number of the task to mask as complete: "))
            complete_task(task_number)     
        elif choice == "3":
            display_incomplete_tasks()
            task_number = int(input("Enter the number of the task to remove: "))
            remove_task(task_number)
        elif choice == "4":
            display_incomplete_tasks()
        elif choice == "5":
            display_completed_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    todolist()
