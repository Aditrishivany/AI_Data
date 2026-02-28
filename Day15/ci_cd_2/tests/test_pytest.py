# from app.calculator import add, subtract, get_api_status

# def test_add():
#     assert add(2, 3) == 5

# def test_subtract():
#     assert subtract(5, 3) == 2

# def test_api():
#     assert get_api_status() == 200
import math
import pytest
import os
import sys
from unittest.mock import patch

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    factorial,
    sine,
    cosine,
    tangent,
    logarithm,
    get_pi,
    get_e,
    get_api_status
)


# -------------------
# BASIC
# -------------------

def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# -------------------
# SCIENTIFIC
# -------------------

def test_power():
    assert power(2, 3) == 8


def test_square_root():
    assert square_root(25) == 5


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-1)


def test_factorial():
    assert factorial(5) == 120


def test_sine():
    assert sine(0) == 0


def test_cosine():
    assert cosine(0) == 1


def test_tangent():
    assert tangent(0) == 0


def test_logarithm():
    assert logarithm(100, 10) == 2


# -------------------
# CONSTANTS
# -------------------

def test_pi():
    assert math.isclose(get_pi(), math.pi)


def test_e():
    assert math.isclose(get_e(), math.e)


# -------------------
# API
# -------------------

def test_api():
    with patch('app.calculator.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        assert get_api_status() == 200