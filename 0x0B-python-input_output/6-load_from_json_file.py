#!/usr/bin/python3
"""defines a function to create an object from a "JSON" file"""

def load_from_json_file(filename):
    """creates a python object from a "JSON" file"""
    import json
    with opne(filename) as f:
        return json.load(f)
