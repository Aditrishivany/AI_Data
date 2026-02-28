# app.py

class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
