#1. Prime Number (Recursive Check)

import math

def prime(a, n=2):
    if a <= 1:
        return False
    if n > math.sqrt(a):
        return True
    if a % n == 0:
        return False
    return prime(a, n + 1)

if prime(10):
    print("prime")
else:
    print("not prime")

#2. CLI Calculator

def calculator():
    print("=== CLI Calculator ===")
    print("Available operations:")
    print("+  -  *  /  //  %  **")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator: ")
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    elif op == "//":
        print(a // b)
    elif op == "%":
        print(a % b)
    elif op == "**":
        print(a ** b)
    else:
        print("Invalid operator")

calculator()

#3. Form Validator (Name, Age, Email, Password)

email = input("Enter your email: ")
password = input("Enter your password: ")
name = input("Enter your name: ")
age = input("Enter your age: ")

emailisvalid = "@" in email and "." in email and email.index("@") < email.index(".")
passwordisvalid = len(password) > 6
nameisvalid = name.isalpha() and len(name) >= 2
ageisvalid = age.isdigit() and int(age) > 0

if emailisvalid and passwordisvalid and nameisvalid and ageisvalid:
    print("Form submitted successfully!")
else:
    print("Form invalid:")
    if not emailisvalid:
        print("- Invalid email")
    if not passwordisvalid:
        print("- Password length must be > 6")
    if not nameisvalid:
        print("- Invalid name")
    if not ageisvalid:
        print("- Invalid age")

#4. sys.argv – print program name & arguments

import sys

print("prog name:", sys.argv[0])
for i in range(1, len(sys.argv)):
    print(f"arg{i}:", sys.argv[i])

5. Script runs only if more than 2 arguments

import sys

if len(sys.argv) > 3:
    print("Running the program...")
    for i in range(1, len(sys.argv)):
        print(f"arg{i}:", sys.argv[i])
else:
    print("Not enough arguments! Need more than 2.")

#6. Backup a File

import shutil
import datetime

source = "D:/Users/Admin/Desktop/data.txt"
backup = f"D:/Users/Admin/Desktop/data_backup_{datetime.date.today()}.txt"

shutil.copy(source, backup)
print(f"Backup of {source} created at {backup}")

#7. Auto-create main folder → subfolder → backup file

import shutil
import datetime
import os

source = "D:/Users/Admin/Desktop/data.txt"

main_folder = "D:/Users/Admin/Desktop/Backups"
if not os.path.exists(main_folder):
    os.mkdir(main_folder)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
subfolder = f"{main_folder}/backup_{timestamp}"
os.mkdir(subfolder)

backup_file = f"{subfolder}/data_backup_{timestamp}.txt"
shutil.copy(source, backup_file)

print(f"Backup created at: {backup_file}")

#8. Backup Only JPG Files

import os
import shutil

source_folder = "D:/Users/Admin/Desktop/Images"
backup_folder = "D:/Users/Admin/Desktop/backup_jpg"

if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        shutil.copy(f"{source_folder}/{file}", f"{backup_folder}/{file}")
        print("Copied:", file)

print("Backup complete.")

#9. To-Do List App (Add/View Tasks)

choice = input("Enter 1 to add task, 2 to view tasks: ")

if choice == "1":
    task = input("Enter task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added")

elif choice == "2":
    with open("tasks.txt", "r") as f:
        print("Your tasks:")
        print(f.read())

#10. Command-line Greeting

import sys
var = sys.argv[1]
bar = sys.argv[2]
print(f"Hello, {var}, {bar}")
