import re
username = input("Enter username: ")
username_pattern = r"^[A-Za-z][A-Za-z0-9_]{2,14}$"
if re.fullmatch(username_pattern, username):
    print("Username is valid")
else:
    print("Username is invalid")
password = input("Enter password: ")
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%!&*]).{8,}$"
if re.fullmatch(password_pattern, password):
    print("Password is strong")
else:
    print("Password is weak")
