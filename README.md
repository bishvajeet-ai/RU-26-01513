
# To-Do List Application

A menu-driven to-do list program written in Python 3 (PS No. 12). It runs in the console and lets you add, view, complete and delete tasks. Every change is saved to a file, so your tasks are still there the next time you run the program.

**Submitted by:** Bishvajeet Srivastav (ERP No. RU-26-01513)
**Guide:** Arjit Singh
**Course:** B.Tech CSE with AI and ML, in association with Google
**Subject:** Programming Fundamentals and Logic Building Using Python

## Features

- Add a new task (every new task starts as Pending)
- View all tasks with their number, title and status
- Mark a task as completed (Done)
- Delete a task
- Tasks are saved to `todo.txt` after every change and loaded when the program starts
- Input checks for an empty title, a wrong or non-numeric task number, a wrong menu option and a missing file

## Concepts Used

- **Lists:** all tasks are stored as `[title, status]` inside one list
- **Functions:** separate functions for load, save, add, view, complete and delete
- **Loops:** a `while` loop keeps the menu running until Exit
- **File handling:** `open()`, read and write to `todo.txt`

## Requirements

- Python 3 (tested on Python 3.12)
- No external libraries are needed

## How to Run

1. Download `todo.py` and keep it in a folder.
2. Open Command Prompt or Terminal in that folder.
3. Run:

```
python todo.py
```

On Mac or Linux, use `python3 todo.py`.

## Menu

```
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
```

## Example

```
Choose an option: 1
Task: Buy books
Task added.
1 | Buy books | Pending
Choose an option: 3
Task number: 1
Task 1 marked as completed.
Choose an option: 2
1 | Buy books | Done
```

## File Format

Each line in `todo.txt` is stored as `status|title`, for example:

```
Done|Buy books
Pending|Pay bill
```

## Testing

All four test cases from the problem statement pass: normal input, an empty list, invalid input (task number 5 and an empty title) and a different valid scenario (complete, view and delete).

## Project Files

- `todo.py`: the complete program
- `todo.txt`: created automatically when you add the first task
