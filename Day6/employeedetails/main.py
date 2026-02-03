import employees

name = input("Enter employee name to search: ")

emp = employees.search_employee(name)

if emp:
    print("\nEmployee Found:")
    print(f"ID: {emp['id']}")
    print(f"Name: {emp['name']}")
    print(f"Department: {emp['department']}")

    print(f"Salary: {emp['salary']}\n")
else:
    print("Employee not found.")
