import math

def add(a, b):
    result = a + b
    print("Operation completed — result saved to database.")
    return result

def subtract(a, b):
    result = a - b
    print("Operation completed — result saved to database.")
    return result

def multiply(a, b):
    result = a * b
    print("Operation completed — result saved to database.")
    return result

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    print("Operation completed — result saved to database.")
    return result

def power(base, exp):
    result = base ** exp
    print("Operation completed — result saved to database.")
    return result

def square_root(num):
    if num < 0:
        raise ValueError("Cannot take square root of a negative number")
    result = math.sqrt(num)
    print("Operation completed — result saved to database.")
    return result

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = math.factorial(n)
    print("Operation completed — result saved to database.")
    return result
