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

## Problems Faced and Solutions

### 1. Duplicate Tasks

**Problem:**  
The same task could be added more than once.

**Solution:**  
I added a check using `if task in tasks` to prevent duplicate tasks.

### 2. Empty Task Names

**Problem:**  
The user could enter an empty task or only spaces.

**Solution:**  
I used `.strip()` and checked whether the task was empty before adding it.

### 3. Task Not Found

**Problem:**  
The program needed to handle cases where a user tried to complete or delete a task that did not exist.

**Solution:**  
I used `if task not in tasks` to check whether the task existed and used `return` to stop the function when it was not found.

### 4. Tasks Were Lost After Closing the Program

**Problem:**  
The tasks stored in the dictionary disappeared when the program was closed.

**Solution:**  
I used JSON file handling with `json.dump()` to save the tasks and `json.load()` to load them again when the program starts.

### 5. JSON File Did Not Exist

**Problem:**  
On the first run, `tasks.json` did not exist, which could cause a `FileNotFoundError`.

**Solution:**  
I used `try` and `except FileNotFoundError` to start with an empty dictionary when the file was not found.

### 6. Counting Pending Tasks

**Problem:**  
The program needed to count how many tasks were still pending.

**Solution:**  
I created a function that loops through the tasks, checks for the `Pending` status, and increases a counter.

## Project Structure

To-Do-Task-Manager/
│
├── todo.py
├── tasks.json
└── README.md

## Purpose

This project was created as a Python practice project to strengthen programming fundamentals and understand how different Python concepts work together in a small real-world application.