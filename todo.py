# TASK: To-Do List: Build a command-line to-do list manager where you can add tasks, mark them as completed, and remove them.
# FUNCTIONALITY:
# - Runs in its own terminal window
# - Tasks can either be incomplete; completed; or removed.
# - Incomplete tasks have been added by user but not marked complete or removed. They are typically displayed.
# - Completed tasks are ones that are marked complete by the user but not deleted. They remain in-app, but are not displayed unless requested.
# - Removed tasks are ones that the user marks for deletion. They are deleted from memory. Users are prompted if they are sure they want them to be deleted.

tasks = []
completed_tasks = []

def add_task(task):
    tasks.append(task)

def complete_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        task = tasks.pop(task_index - 1)
        completed_tasks.append(task)
    else:
        print("Invalid task number. Please enter a valid task number.")

def remove_task(task_index):
    if task_index >=1 and task_index <= len(tasks):
        confirm = input(f"Are you sure you want to delete task {task_index}? (yes/no): ").lower()
        if confirm == "yes":
            tasks.remove(task)
            print("Task removed.")
        else:
            print("Task not deleted.")
    else:
        print("Task number not found. Please enter a valid task number.")

def display_incomplete_tasks():
    print("\n**********")
    print("Incomplete Tasks:")
    if len(tasks) == 0:
        print("No tasks!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def display_completed_tasks():
    print("\n**********")
    print("Completed Tasks:")
    if len(completed_tasks) < 1:
        print("No tasks!")
    else:
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task}")

def main():
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
            task_index = int(input("Enter the number of the task to mark as complete: "))
            complete_task(task_index)
        elif choice == "3":
            display_incomplete_tasks()
            task_index = int(input("Enter the number of the task to remove: "))
            remove_task(task_index)
        elif choice == "4":
            display_incomplete_tasks()
        elif choice == "5":
            display_completed_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
     