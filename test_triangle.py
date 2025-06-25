import unittest
from triangle import is_triangle

class TestTriangleFunction(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(is_triangle(3, 4, 5))

    def test_invalid_triangle(self):
        self.assertFalse(is_triangle(1, 2, 3))

    def test_zero_side(self):
        self.assertFalse(is_triangle(0, 2, 3))

    def test_negative_side(self):
        self.assertFalse(is_triangle(-1, 2, 3))

    def test_all_equal_sides(self):
        self.assertTrue(is_triangle(5, 5, 5))

    def test_two_equal_sides(self):
        self.assertTrue(is_triangle(5, 5, 8))

    def test_float_values(self):
        self.assertTrue(is_triangle(2.5, 2.5, 4.0))

if __name__ == '__main__':
    unittest.main()
