#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest

from models.base import Base
from io import StringIO
from unittest.mock import patch
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
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)
