# To-Do List Application (PS No. 12

FILE_NAME = "todo.txt"


# File handling

def load_tasks():
    """Read tasks from todo.txt and return them as a list."""
    tasks = []
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split("|", 1)       # split into status and title
                status = parts[0]
                title = parts[1]
                tasks.append([title, status])
        file.close()
    except FileNotFoundError:
        # file does not exist yet, so we start with an empty list
        pass
    return tasks


def save_tasks(tasks):
    """Write all tasks into todo.txt (called after every change)."""
    file = open(FILE_NAME, "w")
    for task in tasks:
        file.write(task[1] + "|" + task[0] + "\n")
    file.close()


# Main functions

def add_task(tasks):
    title = input("Task: ").strip()
    if title == "":
        print("Task title cannot be empty.")
        return
    tasks.append([title, "Pending"])      # every new task starts as Pending
    save_tasks(tasks)
    number = len(tasks)
    print("Task added.")
    print(number, "|", title, "|", "Pending")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found. Your to-do list is empty.")
        return
    number = 1
    for task in tasks:
        print(number, "|", task[0], "|", task[1])
        number = number + 1


def complete_task(tasks):
    text = input("Task number: ")
    if not text.isdigit():
        print("Please enter a valid number.")
        return
    number = int(text)
    if number < 1 or number > len(tasks):
        print("Task number", number, "not found.")
        return
    tasks[number - 1][1] = "Done"
    save_tasks(tasks)
    print("Task", number, "marked as completed.")


def delete_task(tasks):
    text = input("Task number: ")
    if not text.isdigit():
        print("Please enter a valid number.")
        return
    number = int(text)
    if number < 1 or number > len(tasks):
        print("Task number", number, "not found.")
        return
    tasks.pop(number - 1)
    save_tasks(tasks)
    print("Task", number, "deleted. Tasks left:", len(tasks))


# Menu loop

tasks = load_tasks()

while True:
    print()
    print("===== To-Do List =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        complete_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1 to 5.")
