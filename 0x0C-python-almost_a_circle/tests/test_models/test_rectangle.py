#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest

from models.base import Base
from models.rectangle import Rectangle


class Test_a_Rectangle(unittest.TestCase):
    """testing functions for Rectangle class"""

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

