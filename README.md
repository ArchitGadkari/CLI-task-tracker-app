# TaskMaster CLI

A simple and efficient command-line task manager built with Python, Typer, and Rich.

## 📜 Description

TaskMaster CLI is a tool to help you manage your to-do list directly from your terminal. You can add new tasks, update existing ones, mark them as in-progress or done, and list them out, all without leaving your command line.

Tasks are stored locally in a tasks_data.json file, making the application portable and easy to back up.

## ✨ Features

Add Tasks: Quickly add a new task to your list.
Update Tasks: Edit the description of an existing task.
Delete Tasks: Remove a task by its ID.
Change Status: Mark tasks as todo, in-progress, or done.
Rich Tables: View all your tasks in a clean, beautifully formatted table thanks to the rich library.
Filter by Status: List only the tasks that are todo, in-progress, or done.

## ⚙️ Requirements

Python 3.7+
Typer
Rich

## 🚀 Installation

Clone the repository (or download the files):

```
git clone https://your-repository-url-here/taskmaster-cli.git
cd taskmaster-cli
```

Install the required packages:
```
pip install -r requirements.txt
```

## 🖥️ Usage

All commands are run from your terminal using the main Python script.

(Assuming your file is named `main.py`)

### 1. Getting Help

To see a full list of commands and options, you can run:
```
python main.py --help
```

### 2. Adding a Task

Use the add command. The status is optional and defaults to todo.
```
# Add a simple task
python main.py add "Write the README file"

# Add a task and set its status
python main.py add "Start coding the new feature" --status in-progress
```

### 3. Listing Tasks

Use the list command. Running it with no arguments shows all tasks.
```
# List all tasks
python main.py list
```

You can also filter by status:
```
# List only tasks that are 'done'
python main.py list done

# List only tasks 'in-progress'
python main.py list in-progress
```

### 4. Updating a Task Description

Use the update command with the task's ID and the new description.
```
# Update the description for task with ID 2
python main.py update 2 "Write a *better* README file"
```

### 5. Marking a Task as "In Progress"

Use the mark-in-progress command with the task's ID.
```
python main.py mark-in-progress 1
```

### 6. Marking a Task as "Done"

Use the mark-done command with the task's ID.
```
python main.py mark-done 1
```

### 7. Deleting a Task

Use the delete command with the task's ID.
```
python main.py delete 3
```

💾 Data Storage

This application is file-based. All your tasks are saved in a file named tasks_data.json created in the same directory as the script. You can back up this file to save your tasks.
