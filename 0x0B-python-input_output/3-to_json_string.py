#!/usr/bin/python3
"""defines function to return JSON representatin of an object"""

import json

def to_json_string(my_obj):
    """returns JSON representation of an object"""
    return json.dumps(my_obj)
