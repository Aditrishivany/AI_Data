class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def display(self, *args):
        if len(args) == 0:
            print(f"Employee ID: {self.emp_id}")
            print(f"Name       : {self.name}")
            print(f"Age        : {self.age}")
            print(f"Salary     : Rs.{self.salary}")

        elif len(args) == 1:
            if args[0] == "basic":
                print(f"{self.emp_id} - {self.name}")
            elif args[0] == "salary":
                print(f"{self.name}'s Salary: Rs.{self.salary}")
            
            else:
                print("Unknown display type!")

        elif len(args) == 2:
            print(f"{args[0]}: {self.name}, {args[1]}: Rs.{self.salary}")

        else:
            print("Too many arguments!")

class Manager(Employee):    
    def __init__(self, emp_id, name, age, salary, dept):
        super().__init__(emp_id, name, age, salary)
        self.dept = dept

    def display(self, *args):
        #print("Manager Details")
        super().display()  
        print(f"Department : {self.dept}")
        print()


eid = input("Enter employee ID: ")
name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
dept = input("Enter department (for Manager): ")

e1 = Employee(eid, name, age, salary)
m1 = Manager(eid, name, age, salary, dept)

print("\nEmployee")
e1.display()

print("\nManager")
m1.display()
