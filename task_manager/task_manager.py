import json

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f'Task(id={self.id}, title="{self.title}", completed={self.completed})'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(task_dict):
        return Task(task_dict['id'], task_dict['title'], task_dict['completed'])

tasks = []

def add_task(title):
    task_id = len(tasks) + 1
    task = Task(task_id, title)
    tasks.append(task)
    print(f'Task "{title}" added.')

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "Completed" if task.completed else "Not Completed"
            print(f'{task.id}. {task.title} [{status}]')

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f'Task {task_id} deleted.')

def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f'Task {task_id} marked as completed.')
            break
    else:
        print(f'Task {task_id} not found.')

def save_tasks(filename="tasks.json"):
    with open(filename, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f)
    print("Tasks saved.")

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, 'r') as f:
            loaded_tasks = json.load(f)
            for task_data in loaded_tasks:
                task = Task.from_dict(task_data)
                tasks.append(task)
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")

def show_menu():
    print("\nTask Manager")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Mark a task as completed")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Exit")

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            load_tasks()
        elif choice == '7':
            save_tasks()
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
