#!/usr/bin/python3
"""defines a function that returns the JSON
representation of a string"""


import json



def to_json_string(my_obj):
    """returns the JSON representation of a string"""
    return json.dumps(my_obj)
