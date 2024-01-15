#!/usr/bin/python3
"""unittest for Base class"""


import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """testing functions for Base class"""

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_base(self):
        """test initialization of id if id None and if id int"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
