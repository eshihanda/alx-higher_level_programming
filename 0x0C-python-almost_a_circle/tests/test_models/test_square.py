#!/usr/bin/python3
""" unit test for square class """


import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """test class for square"""

    def setUp(self):
        """set nb_objects attr to zero before each test"""
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """check if square is instance of Base and Rect """
        s = Square(1)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_square_instantiation(self):
        """test initialization of square instance"""
        r1 = Square(10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Square(10, 55, 81)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 55)
        self.assertEqual(r2.y, 81)
        r3 = Square(20, 45, 16, 70)
        self.assertEqual(r3.id, 70)
        self.assertEqual(r3.width, 20)
        self.assertEqual(r3.height, 20)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 16)
        r4 = Square(60)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r4.width, 60)
        self.assertEqual(r4.height, 60)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test__arguments_passed(self):
        """check if number of arg is right """
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5)

    def test_printing(self):
        """check overloading of __str__ """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 5, 1)
        self.assertEqual(s2.__str__(), "[Square] (1) 5/1 - 5")
        s3 = Square(1, 2)
        self.assertEqual(s3.__str__(), "[Square] (2) 2/0 - 1")
        output = io.StringIO()
        sys.stdout = output
        s1 = Square(4, 2, 1, 12)
        print(s1)
        self.assertEqual(output.getvalue(), "[Square] (12) 2/1 - 4\n")
        sys.stdout = sys.__stdout__

    def test_getter_method_size(self):
        """ check getter width """
        s = Square(20)
        self.assertEqual(s.size, 20)

    def test_setter_method_size(self):
        """ check setter method """
        s = Square(1)
        s.size = 3
        self.assertEqual(s.size, 3)

    def test_valide_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """
        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_display(self):
        """ 10 test for display method """
        output = io.StringIO()
        sys.stdout = output
        s = Square(3)
        s.display()
        self.assertEqual(output.getvalue(), "###\n###\n###\n")
        with self.assertRaises(TypeError):
            s.display(2)
        with self.assertRaises(TypeError):
            s.display(2, 3)
        s = Square(1, 4)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        self.assertEqual(output.getvalue(), "    #\n")

        s = Square(2, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")

        s = Square(2, 1, 0)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        self.assertEqual(output.getvalue(), " ##\n ##\n")
        sys.stdout = sys.__stdout__

    def test_update_args_kwargs(self):
        """ 12 test for args and kwars on update method """
        s = Square(10, 10, 10)
        s.update(1, y=2, x=3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)
        self.assertEqual(s.size, 10)
        s.update(1, size=3)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.id, 1)
        s = Square(1, 2, 3, 4)
        dic = {"size": 30, "x": 40, "y": 50, "id": 60}
        s.update(1, 2, 3, 4, dic)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        s.update(**dic)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 40)
        self.assertEqual(s.y, 50)
        self.assertEqual(s.id, 60)
        lis = (1, 2, 3, 4)
        s.update(*lis, **dic)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        s.update(**dic)
        self.assertEqual(s.id, 60)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 40)
        self.assertEqual(s.y, 50)
        s.update(y=1, size=2, x=3, id=5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 1)
        s.update(size=10)
        s.update(x=10)
        s.update(y=10)
        s.update(id=10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

