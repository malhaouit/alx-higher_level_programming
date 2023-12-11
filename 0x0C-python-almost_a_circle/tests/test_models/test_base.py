import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_no_argument(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_with_argument(self):
        b2 = Base(30)
        self.assertEqual(b2.id, 30)

    def test_id_increment(self):
        b3 = Base()
        b4= Base()
        self.assertEqual(b3.id, 1)
        self.assertEqual(b4.id, 2)

    def test_id_arguments_and_no_arguments(self):
        b5 = Base(35)
        b6 = Base()
        b7 = Base(40)
        b8 = Base()
        b9 = Base()
        self.assertEqual(b5.id, 35)
        self.assertEqual(b6.id, 1)
        self.assertEqual(b7.id, 40)
        self.assertEqual(b8.id, 2)
        self.assertEqual(b9.id, 3)

    def test_id_assignement(self):
        b10 = Base(10)
        b10.id = 15
        self.assertEqual(b10.id, 15)

    def test_multiple_arguments(self):
        with self.assertRaises(TypeError):
            b11 = Base(1, 1)

    def test_access_private_class_attribute(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_id_with_no_integer(self):
        b12 = Base('100')
        self.assertEqual(b12.id, "100")
