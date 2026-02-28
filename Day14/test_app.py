# test_app.py

import pytest
from app import Calculator

@pytest.fixture
def calc():
    return Calculator()

# Basic tests
def test_add(calc):
    assert calc.add(2, 3) == 5

def test_sub(calc):
    assert calc.sub(5, 3) == 2

def test_multiply(calc):
    assert calc.multiply(4, 3) == 12

def test_division(calc):
    assert calc.division(10, 5) == 2

# Edge case
def test_division_by_zero(calc):
    with pytest.raises(ValueError):
        calc.division(10, 0)

# Parameterized test
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (4, 5, 9),
    (7, 8, 15),
    (-1, -2, -3),
    (0, 5, 5)
])
def test_add_param(calc, a, b, expected):
    assert calc.add(a, b) == expected
