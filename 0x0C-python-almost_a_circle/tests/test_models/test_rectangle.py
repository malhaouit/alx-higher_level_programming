import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        r = Rectangle(10, 15, 2, 3, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_validation(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-10, 10)

    def test_non_integer_width_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 10)
        with self.assertRaises(TypeError):
            r = Rectangle(10, "10")

    def test_non_integer_x_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, "2", 3)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, 2, "3")

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(10, -10)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 10, -2, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 10, 2, -3)

    def test_display(self):
        r = Rectangle(2, 2, 2, 2)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")
