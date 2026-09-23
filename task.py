import json                     # import module ko use karna


# Dictionary for practice

# tasks = {
#     "Learn Python": "Completed",
#     "Practice SQL": "Pending",
#     "Build API": "Pending",
#     "Read Book": "Completed"
# }


# try risky code ko try karna
try:
    # with → safe file handling
    # open() → file open karna
    # as → file ko variable name dena
    with open("tasks.json") as file:

        # json.load() → JSON file se data read karna
        tasks = json.load(file)

# except exception/error handle karna
# FileNotFoundError file nahi mili
except FileNotFoundError:
    tasks = {}                  # empty dictionary


# def function define karna
def count_pending_tasks(tasks):

    count = 0                   

    # for loop
    # .items() dictionary ke key-value pairs
    for task, status in tasks.items():

        # if condition
        # == comparison
        if status == "Pending":

            # += value increase karna
            count += 1

    # return value wapas dena
    return count


# Function
def add_task(tasks, task):

    # in membership check
    if task in tasks:
        print("Task already exists")

    # else condition false hone par
    else:
        tasks[task] = "Pending"


# Function
def complete_task(tasks, task):

    # not condition ko reverse karna
    # in membership check
    if task not in tasks:
        print("Task not found")

        # return function ko stop karna
        return

    if tasks[task] == "Pending":
        tasks[task] = "Completed"

    else:
        print("Task is already completed")


# Function
def delete_task(tasks, task):

    if task not in tasks:
        print("Task is not found")
        return

    # del dictionary se item delete karna
    if task in tasks:
        del tasks[task]


# Function
def view_tasks(tasks):

    # not empty dictionary check
    if not tasks:
        print("No tasks found")

    else:
        print("----- All Tasks -----")

        # for loop
        # .items() key-value pairs
        for task, status in tasks.items():
            print(f"{task} → {status}")


# while loop
while True:

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Pending Tasks")
    print("6. Exit")

    # input() user input
    choice = input("Enter your choice: ")


    # if condition
    if choice == "1":

        task = input("Enter task: ")

        # .strip() beginning/end ke extra spaces remove
        task = task.strip()

        if task == "":
            print("Task cannot be empty")

        else:
            # Function call
            add_task(tasks, task)


    # elif another condition
    elif choice == "2":

        # Function call
        view_tasks(tasks)


    elif choice == "3":

        task = input("Enter task: ")
        task = task.strip()

        if task in tasks:
            complete_task(tasks, task)

        else:
            print("Task not found")


    elif choice == "4":

        task = input("Enter task: ")
        task = task.strip()

        if task in tasks:
            delete_task(tasks, task)

        else:
            print("Task not found")


    elif choice == "5":

        # Function call + returned value
        result = count_pending_tasks(tasks)

        # f-string variable ko string ke andar use karna
        print(f"Pending tasks: {result}")


    elif choice == "6":

        # File save
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

        # break loop ko stop karna
        break


    # Invalid input
    else:
        print("Invalid choice")