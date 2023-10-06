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

def remove_task(task):
    task_list.remove(task)

def complete_task(task):
    completed_task_list.append(task)
    task = f"COMPLETED - {task}"

def todolist():
    # GET USER CHOICE: ADD TASK? REMOVE TASK? MARK TASK COMPLETE?


if __name__ == "__main__":
    todolist()
