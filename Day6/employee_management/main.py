from decorators.access import registration, login
from employee.details import show_employee
@registration
def register(name,email,phone,designation,salary):
    show_employee(name,email,phone,designation,salary)
@login
def user_login(username,login_status):
    print("Accessing Dashboard...")
register("Aditri","aditri@example.com",9876543210,"HR Manager",60000)
user_login("Aditri", True)