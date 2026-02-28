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
