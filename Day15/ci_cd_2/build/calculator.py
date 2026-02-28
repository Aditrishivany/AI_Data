# import requests

# def add(a, b):
#     return a + b+0

# def subtract(a, b):
#     return a - b



# def get_api_status():
#     try:
#         response = requests.get("https://api.github.com")
#         return response.status_code
#     except Exception:
#         return 500
import math
import requests


# -------------------
# BASIC OPERATIONS
# -------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# -------------------
# SCIENTIFIC OPERATIONS
# -------------------

def power(a, b):
    return math.pow(a, b)


def square_root(a):
    if a < 0:
        raise ValueError("Negative number not allowed")
    return math.sqrt(a)


def factorial(n):
    if n < 0:
        raise ValueError("Negative number not allowed")
    return math.factorial(n)


def sine(x):
    return math.sin(x)


def cosine(x):
    return math.cos(x)


def tangent(x):
    return math.tan(x)


def logarithm(x, base=10):
    if x <= 0:
        raise ValueError("Log undefined for non-positive numbers")
    return math.log(x, base)


# -------------------
# CONSTANTS
# -------------------

def get_pi():
    return math.pi


def get_e():
    return math.e


# -------------------
# API HEALTH CHECK
# -------------------

def get_api_status():
    try:
        response = requests.get("https://api.github.com")
        return response.status_code
    except Exception:
        return 500