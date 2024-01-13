#!/usr/bin/python3
"""defines a function that returns the object
represented by a json string"""


import json


def from_json_string(my_str):
    """returns the object(python data structure)
    represented by a json string"""
    return json.loads(my_str)
