# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello!")

# greet()

# # decorator with arguments
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"\nCalling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def add(a, b):
#     return a + b

# print(add(5, 7))
# print()

# # decorator with parameter
# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
# @repeat(3)
# def hello():
#     print("Hello!")
# hello()
# print()

# # static method
# class Demo:
#     @staticmethod
#     def greet():
#         return "Hi"
# print(Demo.greet())
# obj=Demo()
# print(obj.greet())

# #class method
# class Student:
#     school_name="ABC High School"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def change_school_name(cls,new_name):
#         cls.school_name=new_name
# print("\nBefore change:",Student.school_name)
# Student.change_school_name("XYZ High School")
# print("After change:",Student.school_name)


#property method
class person:
    def __init__(self,name):
        self.name=name
    @property
    def name(self):
        return self.__name 
    @name.setter
    def name(self,value):
        if value<0:
            raise ValueError("")
        self._name=value
p=person("Aditri")
print(p.name)

#decorator to print salary and designation
# def designation_decorator(func):
#     def wrapper(name, designation, salary):
#         print("Designation:", designation) 
#         func(name, designation, salary)
#     return wrapper
# def salary_decorator(func):
#     def wrapper(name, designation, salary):             
#         func(name, designation, salary)
#         print("Salary:", salary)
#     return wrapper
# @salary_decorator
# @designation_decorator
# def employee(name, designation, salary):
#     print("Employee details displayed")
# employee("Aditri","HR",500000)

# #user login using decorators
# def login(func):
#     def wrapper(username, login_status):
#         if login_status:
#             print(f"\nLogin Successful, {username}")
#             func(username, login_status)
#         else:
#             print(f"\nLogin Failed, {username}")
#     return wrapper
# @login
# def userlogin(username, login_status):
#     print("Welcome to dashboard")
# userlogin("Aditri",True)
# userlogin("Siri",False)

# registration using decorators
# def registration(func):
#     def wrapper(name, email, phone):
#         if not name.strip():
#             print("Invalid Name")
#             return
#         if "@" not in email and "." not in email:
#             print("Invalid Email")
#             return
#         if len(str(phone)) != 10:
#             print("Invalid Phone Number")
#             return
#         func(name, email, phone)
#     return wrapper
# @registration
# def register_user(name, email, phone):
#     print("Registration Successful!")
#     print(f"Name: {name}")
#     print(f"Email: {email}")
#     print(f"Phone: {phone}")
# register_user("aditri","Aditrishivany116@gmail.com",9000055050)