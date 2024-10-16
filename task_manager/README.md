# Task Manager CLI Application

## Project Description
The **Task Manager CLI Application** is a command-line tool that allows users to manage their daily tasks efficiently. It provides functionalities to add, view, delete, and mark tasks as completed. The application also supports saving and loading tasks from a file, making it easy to persist and retrieve tasks between sessions.

## How to Run the Application
To run the application, follow these steps:

1. Clone or download the project files.
2. Navigate to the project directory (`task_manager`) using the terminal.
3. Ensure you have Python installed on your system (Python 3.x recommended).
4. Run the application by executing the following command:


## Overview of Functionalities

1. **Add a Task**: Allows the user to input a task title and add it to the task list.
2. **View Tasks**: Displays all tasks with their status (Completed/Not Completed).
3. **Delete a Task**: Allows the user to remove a task by specifying its ID.
4. **Mark Task as Completed**: Allows the user to mark a task as completed.
5. **Save Tasks**: Saves the current list of tasks to a file (`tasks.json`).
6. **Load Tasks**: Loads tasks from the `tasks.json` file upon starting the application.
7. **Exit**: Safely exits the application, saving tasks before exiting.

## Usage Instructions

Once the application is running, you will be presented with a menu to choose from the following options:

1. Add a new task
2. View tasks
3. Delete a task
4. Mark a task as completed
5. Save tasks
6. Load tasks
7. Exit

You can choose an option by entering the corresponding number.

## Example:

```bash
Task Manager
1. Add a new task
2. View tasks
3. Delete a task
4. Mark a task as completed
5. Save tasks
6. Load tasks
7. Exit

Enter your choice: 1
Enter task title: Buy groceries
Task "Buy groceries" added.

Enter your choice: 2
1. Buy groceries [Not Completed]

Enter your choice: 4
Enter task ID to mark as completed: 1
Task 1 marked as completed.

Enter your choice: 2
1. Buy groceries [Completed]
