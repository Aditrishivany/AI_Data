class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def display(self):
        print(f"name:{self.name}, age:{self.age}")
name=input("enter name:")
age=int(input("enter age:"))
s1=Student(name,age)
s1.display()