# To-Do Task Manager

A simple Python To-Do Task Manager built to practice Python fundamentals, functions, file handling, JSON, loops, conditions, and basic data management.

## Features

- Add new tasks
- Prevent duplicate tasks
- View all tasks with their status
- Mark tasks as completed
- Delete tasks
- Count pending tasks
- Prevent empty task names
- Save tasks to a JSON file
- Load previously saved tasks when the program starts
- Handle missing JSON file using exception handling
- Interactive menu using a while loop

## Concepts Practiced

- Variables and Data Types
- Dictionaries
- Functions
- if, elif, and else
- for and while loops
- break
- in and not in
- return
- input() and print()
- .strip()
- Dictionary methods such as .items()
- File Handling
- JSON
- try and except
- FileNotFoundError
- json.load()
- json.dump()
- f-strings

## How It Works

When the program starts, it tries to load previously saved tasks from the tasks.json file.

If the file does not exist, the program starts with an empty dictionary.

The user can choose different options from the menu:

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Pending Tasks
6. Exit

When the user exits the program, the current tasks are saved to the tasks.json file.

## Example

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Pending Tasks
6. Exit

Enter your choice: 1
Enter task: Learn FastAPI

The task is added with the status:

Learn FastAPI → Pending

After completing it:

Learn FastAPI → Completed

## Project Structure

To-Do-Task-Manager/
│
├── todo.py
├── tasks.json
└── README.md

## Purpose

This project was created as a Python practice project to strengthen programming fundamentals and understand how different Python concepts work together in a small real-world application.