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