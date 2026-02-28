# import unittest
# from app.calculator import add, subtract

# class TestCalculator(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual(add(10, 5), 15)

#     def test_subtract(self):
#         self.assertEqual(subtract(10, 5), 5)

# if __name__ == "__main__":
#     unittest.main()
import unittest
import math
import sys
import os

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
)


class TestCalculator(unittest.TestCase):

    # -------------------
    # BASIC
    # -------------------

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(divide(20, 4), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    # -------------------
    # SCIENTIFIC
    # -------------------

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_sine(self):
        self.assertEqual(sine(0), 0)

    def test_cosine(self):
        self.assertEqual(cosine(0), 1)

    def test_tangent(self):
        self.assertEqual(tangent(0), 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(100, 10), 2)

    # -------------------
    # CONSTANTS
    # -------------------

    def test_pi(self):
        self.assertTrue(math.isclose(get_pi(), math.pi))

    def test_e(self):
        self.assertTrue(math.isclose(get_e(), math.e))


if __name__ == "__main__":
    unittest.main()