def registration(func):
    def wrapper(name, email, phone):
        if "@" not in email or "." not in email:
            print("Invalid Email")
            return
        if len(str(phone)) != 10:
            print("Invalid Phone Number")
            return    
        print(f"\nRegistration Successful — Welcome, {name}!")
        return func(name, email, phone)
    return wrapper
