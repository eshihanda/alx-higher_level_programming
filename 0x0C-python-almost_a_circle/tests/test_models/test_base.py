#!/usr/bin/python3
"""unittest for Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        """ 15 check static method to_json_string BASE """
        b1 = Base()
        b2 = Base()
        lis = [b1.__dict__, b2.__dict__]
        dic = {"id": 1}
        b_json_dict_str = Base.to_json_string([])
        self.assertEqual(b_json_dict_str, "[]")
        b_json_dict_str = Base.to_json_string(None)
        self.assertEqual(b_json_dict_str, "[]")
        b_json_dict_str = Base.to_json_string(lis)
        self.assertNotEqual(type(b_json_dict_str), type(dic))
        self.assertEqual(type(b_json_dict_str), str)
        self.assertEqual(b_json_dict_str, '[{"id": 1}, {"id": 2}]')
