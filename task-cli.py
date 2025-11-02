import json
import typer
from rich.console import Console
from rich.table import Table
import datetime

# This is the main file where our database is stored
DB_FILE = "tasks_data.json"
app = typer.Typer()
console = Console()

def load_tasks_data()->list[dict]:
    """It opens the Database file and loads the data, creates an Empty list if file doesn't exit or any Error happens."""
    try:
        with open(DB_FILE, "r") as file:
            tasks_data:list = json.load(file)
            if isinstance(tasks_data, list):
                return tasks_data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_tasks_data(tasks_data:list[dict])->None:
    """It saves the provided data to the DataBase file."""
    with open(DB_FILE, "w") as file:
        json.dump(tasks_data, file, indent = 4)

def assign_id(tasks_data:list[dict])->int:
    """It evaluated the highest id in our tasks and returns a new id which is (highest + 1)"""
    last_task_index:int = len(tasks_data) - 1
    highest_id:int = tasks_data[last_task_index]["id"]
    new_id:int = highest_id + 1
    return new_id

def assign_current_time()->str:
    """It returns the current date & time as a string."""
    now:datetime = datetime.datetime.now()
    current_time:str = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}:{now.second}"
    return current_time

def print_task_table(filtered_tasks: list[dict], table_title:str)->None:
    """This function prints the table with the required tasks and their properties."""
    table = Table(title= table_title)

    table.add_column("ID.", justify="center", no_wrap=True)
    table.add_column("Task Description", justify="center", no_wrap=True)
    table.add_column("Status", justify="center", no_wrap=True)
    table.add_column("Created at", justify="center", no_wrap=True)
    table.add_column("Updated at", justify="center", no_wrap=True)

    for task in filtered_tasks:
        table.add_row(str(task["id"]) , task["description"], task["status"], task["createdAt"], task["updatedAt"])
    
    console.print(table)

@app.command()
def add(task_description:str, status:str = "todo")->None:
    """This takes task description and status(optional) as input and adds a Task to the Database with its properties."""

    tasks_data:list[dict] = load_tasks_data()
    new_task:dict = {
        "id" : assign_id(tasks_data),
        "description" : task_description,
        "status" : status,
        "createdAt" : assign_current_time(),
        "updatedAt" : assign_current_time(),
    }
    tasks_data.append(new_task)
    console.print(f"Task added successfully (ID: {new_task["id"]})")
    save_tasks_data(tasks_data)

@app.command()
def update(id:int, task_description:str)->None:
    """This takes the id of task and changes its respective task's descrption if it matches."""
    tasks_data:list[dict] = load_tasks_data()
    validTaskId:bool = False
    for task in tasks_data:
        if task["id"] == id:
            task["description"] = task_description
            task["updatedAt"] = assign_current_time()
            save_tasks_data(tasks_data)
            validTaskId = True
            break
    if not validTaskId:
        console.print("Invalid Task ID, Try again!")

@app.command()
def delete(id:int)->None:
    """This takes the id of a task and deletes that task if the id matches."""

    tasks_data = load_tasks_data()
    validTaskId:bool = False
    for index, task in enumerate(tasks_data):
        if task["id"] == id:
            del tasks_data[index]
            console.print(f"Task (ID: {task["id"]}) deleted.")
            save_tasks_data(tasks_data)
            validTaskId = True
            break
    if not validTaskId:
        console.print("Invalid Task ID, Try again!")

@app.command(name = "mark-in-progress")
def mark_in_progress(id:int)->None:
    """This takes id as an input and changes the respective task's status to 'in-progress'"""

    tasks_data = load_tasks_data()
    validTaskId:bool = False
    for task in tasks_data:
        if task["id"] == id:
            task["status"] = "in-progress"
            task["updatedAt"] = assign_current_time()
            console.print(f"Task (ID: {task["id"]}) in progess..")
            save_tasks_data(tasks_data)
            validTaskId = True
            break
    if not validTaskId:
        console.print("Invalid Task ID, Try again!")

@app.command(name = "mark-done")
def mark_done(id:int)-> None:
    """This takes id as an input and changes the respective task's status to 'done'"""

    tasks_data:list[dict] = load_tasks_data()
    validTaskId:bool = False
    for task in tasks_data:
        if task["id"] == id:
            task["status"] = "done"
            task["updatedAt"] = assign_current_time()
            console.print(f"Task (ID: {task["id"]}) is Done..")
            save_tasks_data(tasks_data)
            validTaskId = True
            break
    if not validTaskId:
        console.print("Invalid Task ID, Try again!")

@app.command(name = "list")
def list_tasks(status: str = typer.Argument(None, show_default=False))->None:
    """This takes the status as an optional input and print a table with tasks of that status ELSE print a table with all Tasks."""

    tasks_data = load_tasks_data()
    if status:
        filtered_data = []
        for task in tasks_data:
            if task["status"] == status:
                filtered_data.append(task)
                title = f"Tasks {status}"
        print_task_table(filtered_data, title)
    else:
        filtered_data = tasks_data
        title = f"List of all tasks"
        print_task_table(filtered_data, title)

def main():
    app()

if __name__ == "__main__":
    main()