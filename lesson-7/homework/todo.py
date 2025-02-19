import json
import csv
#made sure that these 2 types are supported
class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'): #by default, there's no due date, and task isnt done
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class TaskManager:
    def __init__(self, file_name='tasks.json', file_format='json'):
        self.file_name = file_name
        self.file_format = file_format
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)
    
    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title if title else task.title
                task.description = description if description else task.description
                task.due_date = due_date if due_date else task.due_date
                task.status = status if status else task.status
                self.save_tasks()
                print("Task updated successfully!")
                return
        print("Task not found.")
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()
        print("Task deleted successfully!")
    
    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if filtered:
            for task in filtered:
                print(task)
        else:
            print("No tasks found with status:", status)
    
    def save_tasks(self):
        if self.file_format == 'json':
            with open(self.file_name, 'w') as file:
                json.dump([task.__dict__ for task in self.tasks], file, indent=4)
        elif self.file_format == 'csv':
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
                for task in self.tasks:
                    writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
        elif self.file_format == 'txt':
            with open(self.file_name, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}\n")
    
    def load_tasks(self):
        try:
            if self.file_format == 'json':
                with open(self.file_name, 'r') as file:
                    tasks_data = json.load(file)
                    self.tasks = [Task(**task) for task in tasks_data]
            elif self.file_format == 'csv':
                with open(self.file_name, 'r') as file:
                    reader = csv.DictReader(file)
                    self.tasks = [Task(row['Task ID'], row['Title'], row['Description'], row['Due Date'], row['Status']) for row in reader]
            elif self.file_format == 'txt':
                with open(self.file_name, 'r') as file:
                    for line in file:
                        task_data = line.strip().split(', ')
                        if len(task_data) == 5:
                            self.tasks.append(Task(*task_data))
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

class ToDoApp:
    def __init__(self):
        file_format = input("Choose file format (json/csv/txt): ").strip().lower()#handled the case where user enters JSON or jSOn instead of json, etc.
        self.manager = TaskManager(file_format=file_format)
    
    def run(self):
        while True:
            print("""
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Filter Tasks
6. Exit
""")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                task = Task(
                    input("Enter Task ID: "),
                    input("Enter Title: "),
                    input("Enter Description: "),
                    input("Enter Due Date (YYYY-MM-DD, optional): ") or None,#if no data is entered, theeres no deadline
                    input("Enter Status (Pending/In Progress/Completed): ") or 'Pending'
                )
                self.manager.add_task(task)
            elif choice == '2':
                self.manager.view_tasks()
            elif choice == '3':
                self.manager.update_task(
                    input("Enter Task ID: "),
                    input("New Title (leave blank to keep current): ") or None,
                    input("New Description (leave blank to keep current): ") or None,
                    input("New Due Date (YYYY-MM-DD, leave blank to keep current): ") or None,
                    input("New Status (Pending/In Progress/Completed, leave blank to keep current): ") or None
                )
            elif choice == '4':
                self.manager.delete_task(input("Enter Task ID to delete: "))
            elif choice == '5':
                self.manager.filter_tasks(input("Enter Status to filter by: "))
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    ToDoApp().run()