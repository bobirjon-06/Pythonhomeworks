import json
import csv

def load_tasks(filename):
    with open(filename, 'r') as file:#readmode
        return json.load(file)

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:#writemode
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks else 0

    print("\nTask Statistics:")
    print("Total tasks:", total_tasks)
    print("Completed tasks:", completed_tasks)
    print("Pending tasks:", pending_tasks)
    print("Average priority:", round(average_priority, 2))

def json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

def main():
    json_file = 'tasks.json'
    csv_file = 'tasks.csv'

    initial_tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]
    save_tasks(json_file, initial_tasks)

    tasks = load_tasks(json_file)
    display_tasks(tasks)
    calculate_stats(tasks)
    json_to_csv(json_file, csv_file)

    print("\nTasks saved to", csv_file)

if __name__ == '__main__':
    main()
