class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
    
class Employeemanager:
    FILE_NAME = "employees.txt"
    def __init__(self):
        open(self.FILE_NAME, 'a').close()
    
    def add_employee(self, emp):
        with open(self.FILE_NAME, 'a') as file:
            file.write(str(emp)+ '\n')
        print("Addded")

    def view_all_employees(self):
        with open(self.FILE_NAME, 'r') as file:
            records = file.readlines()
        if records:
            print("Employee Records:")
            for record in records:
                print(record.strip())
        else:
            print("No employee records found.")

    def update_employee(self, emp_id, name=None, position=None, salary=None):
        updated = False
        with open(self.FILE_NAME, 'r') as file:
            lines = file.readlines()
        with open(self.FILE_NAME, 'w') as file:
            for line in lines:
                if line.startswith(emp_id + ','):
                    parts = line.strip().split(', ')
                    parts[1] = name if name else parts[1]
                    parts[2] = position if position else parts[2]
                    parts[3] = salary if salary else parts[3]
                    file.write(', '.join(parts) + '\n')
                    updated = True
                else:
                    file.write(line)
        print("Employee updated successfully!" if updated else "Employee not found.")

    def delete(self, emp_id, name=None, position = None, salary = None):
        deleted = False
        with open(self.FILE_NAME, 'r') as file:
            lines = file.readlines()
        with open(self.FILE_NAME, 'w') as file:
            for line in lines:
                if not line.startswith(emp_id + ','):
                    file.write(line)
                else:
                    deleted = True
        print("Employee deleted successfully!" if deleted else "Employee not found.")
    def run(self):
        while True:
            print("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")
            choice = input("Enter your choice: ")
            if choice == '1':
                emp = Employee(
                    input("Employee ID: "),
                    input("Name: "),
                    input("Position: "),
                    input("Salary: ")
                )
                self.add_employee(emp)
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                emp_id = input("Enter Employee ID to search: ")
                print(self.search_employee(emp_id))
            elif choice == '4':
                emp_id = input("Enter Employee ID to update: ")
                name = input("New Name (leave blank to keep current): ") or None
                position = input("New Position (leave blank to keep current): ") or None
                salary = input("New Salary (leave blank to keep current): ") or None
                self.update_employee(emp_id, name, position, salary)
            elif choice == '5':
                emp_id = input("Enter employee ID to delete: ")
                self.delete(emp_id)
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

Employeemanager().run()