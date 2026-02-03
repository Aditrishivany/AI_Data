import csv

def load_employees(csv_file="employees.csv"):
    employees = []
    try:
        with open(csv_file, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print("CSV file not found.")
    return employees


def search_employee(name, csv_file="employees.csv"):
    employees = load_employees(csv_file)
    name = name.lower() 
    for emp in employees:
        if emp["name"].lower() == name:
            return emp 

    return None 
