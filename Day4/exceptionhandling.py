try:
    print("step1")
    a=int(input("enter numerator: "))
    b=int(input("enter denominator: "))
    result=a/b
    print("step2")
    print("result=",result)
except Exception as e:
    print("Error: Division by zero is not allowed")