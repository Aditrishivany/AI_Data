def registration(func):
    def wrapper(name,email,phone,designation,salary):
        if "@" not in email or "." not in email:
            print("Invalid Email")
            return
        if len(str(phone)) != 10:
            print("Invalid Phone Number")
            return
        print("Registration Successful")
        func(name,email,phone,designation,salary)
    return wrapper

def login(func):
    def wrapper(username,login_status):
        if login_status:
            print("Login Successful:", username)
            func(username,login_status)
        else:
            print("Login Failed:", username)
    return wrapper
