#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest
import io
import sys
import os

from models.base import Base	
from models.rectangle import Rectangle


class Test_a_Rectangle(unittest.TestCase):
    """testing functions for Rectangle class"""

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """test initialization of rectangle instance"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 60, 50, 80)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 60)
        self.assertEqual(r2.x, 50)
        self.assertEqual(r2.y, 80)
        r3 = Rectangle(20, 89, 45, 10, 70)
        self.assertEqual(r3.id, 70)
        self.assertEqual(r3.width, 20)
        self.assertEqual(r3.height, 89)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 10)
        r4 = Rectangle(40, 100)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r4.width, 40)
        self.assertEqual(r4.height, 100)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test_errors_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            Rectangle("2", 2, 2, 2, 2)

    def test_error_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            Rectangle(2, "2", 2, 2, 2)

    def test_error_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "2", 2, 2)

    def test_error_attrs_4(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 2, "2", 2)

    def test_value_error(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_value_error_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_value_error_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_value_error_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_correct_args(self):
        """ Test for passing one or no argument """
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()

    def test_area(self):
        """test for area method """
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        with self.assertRaises(TypeError):
            r.area(2)
        with self.assertRaises(TypeError):
            r.area(2, 3)

    def test_display(self):
        """ 5 and 7 test for display method """
        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(4, 3)
        r.display()
        self.assertEqual(output.getvalue(), "####\n####\n####\n")

        r = Rectangle(1, 4)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), "#\n#\n#\n#\n")

        r = Rectangle(2, 3, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        
        r = Rectangle(3, 2, 1, 0)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        self.assertEqual(output.getvalue(), " ###\n ###\n")
        sys.stdout = sys.__stdout__

    def test_printing(self):
        """ 6 override __str method """
        r1 = Rectangle(6, 4, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 6/4")
        r2 = Rectangle(4, 6, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 4/6")
        r3 = Rectangle(1, 2)
        self.assertEqual(r3.__str__(), "[Rectangle] (2) 0/0 - 1/2")
        output = io.StringIO()
        sys.stdout = output
        r1 = Rectangle(6, 4, 2, 1, 12)
        print(r1)
        self.assertEqual(output.getvalue(), "[Rectangle] (12) 2/1 - 6/4\n")
        r2 = Rectangle(4, 6, 1)
        output = io.StringIO()
        sys.stdout = output
        print(r2)
        self.assertEqual(output.getvalue(), "[Rectangle] (3) 1/0 - 4/6\n")
        r3 = Rectangle(1, 2)
        output = io.StringIO()
        sys.stdout = output
        print(r3)
        self.assertEqual(output.getvalue(), "[Rectangle] (4) 0/0 - 1/2\n")
        sys.stdout = sys.__stdout__

    def test_update(self):
        """ 8 test for update method """
        r = Rectangle(10, 20, 30, 40, 50)
        r.update()
        self.assertEqual(r.id, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        r.update(89, 90, 91)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 90)
        self.assertEqual(r.height, 91)
        r.update(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        r.update(89, 90, 91, 92, 93)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 90)
        self.assertEqual(r.height, 91)
        self.assertEqual(r.x, 92)
        self.assertEqual(r.y, 93)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        lis = ()
        r.update(*lis)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        lis = (1, 2)
        r.update(*lis)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        lis = (10, 20, 30, 40, 50)
        r.update(*lis)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_args_kwargs(self):
        """8 and 9 test for args and kwars on update method Rectangle"""
        r = Rectangle(10, 10, 10, 10)
        r.update(100, height=2, x=3)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.width, 10)
        r.update(1, 1, 2, width=3, height=4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        r = Rectangle(10, 20, 30, 40, 50)
        dic = {"width": 20, "height": 30, "x": 40, "y": 50, "id": 60}
        r.update(1, 2, 3, 4, 5, dic)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        r.update(**dic)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
        self.assertEqual(r.id, 60)
        lis = [1, 2, 3, 4, 5]
        r.update(*lis, **dic)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        r.update(**dic)
        self.assertEqual(r.id, 60)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
        r.update(y=1, width=2, x=3, height=4, id=5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)
