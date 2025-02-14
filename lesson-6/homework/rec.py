def create_file():
    open("employees.txt", "a").close()

def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        position = input("Position: ")
        salary = input("Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Added!")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            print(*[record.strip() for record in records], sep="\n") if records else print("No records.")
    except FileNotFoundError:
        print("File not found.")

def search_employee():
    emp_id = input("Employee ID: ")
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Found:", record.strip())
                return
    print("Not found.")

def update_employee():
    emp_id = input("Employee ID: ")
    with open("employees.txt", "r") as file:
        records = [record if not record.startswith(emp_id + ",") else f"{emp_id}, {input('Name: ')}, {input('Position: ')}, {input('Salary: ')}\n" for record in file]
    with open("employees.txt", "w") as file:
        file.writelines(records)
    print("Updated!" if any(r.startswith(emp_id + ",") for r in records) else "Not found.")

def delete_employee():
    emp_id = input("Employee ID: ")
    with open("employees.txt", "r") as file:
        records = [record for record in file if not record.startswith(emp_id + ",")]
    with open("employees.txt", "w") as file:
        file.writelines(records)
    print("Deleted!" if len(records) < sum(1 for _ in open("employees.txt")) else "Not found.")

def main():
    create_file()
    options = {
        '1': add_employee,
        '2': view_employees,
        '3': search_employee,
        '4': update_employee,
        '5': delete_employee,
    }
    while True:
        print("\n1. Add | 2. View | 3. Search | 4. Update | 5. Delete | 6. Exit")
        choice = input("Choice: ")
        if choice == '6':
            break
        options.get(choice, lambda: print("Invalid choice."))()
        
if __name__ == "__main__":
    main()
