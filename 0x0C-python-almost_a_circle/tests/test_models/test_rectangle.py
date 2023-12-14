#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest

from models.rectangle import Rectangle


class Test_a_Rectangle(unittest.TestCase):
    """testing functions for Rectangle class"""
    
    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0
    
    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_isinstance(self):
        """ check if rectangle is instance of Base and Rect """
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

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
    def test_errors(self):
       """tests errors raised during initialization"""
       with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Im", 9)
            Rectangle('1', 9)
            Rectangle(True, 8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, "im")
            Rectangle(7, '2')
            Rectangle(7, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, "im")
            Rectangle(5, 4, '1')
            Rectangle(7, 2, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 1, 'im')
            Rectangle(3, 2, 1, "2")
            Rectangle(8, 1, 2, True)

    def test_errors_continue(self):
        """test for width and height ranges"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)
            Rectangle(0, 1)
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, -3)
            Rectangle(2, 0)
            Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 4, -1)
            Rectangle(13, 2, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(7, 6, 5, -3)
            Rectangle(4, 2, 1, 0)

    def test_correct_args(self):
        """ Test for passing one or no argument """
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()

    def test_area_2(self):
        """ Checking the return value of area method """
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)
        r1.width = 6
        self.assertEqual(r1.area(), 12)
        r1.height = 5
        self.assertEqual(r1.area(), 20)

    
