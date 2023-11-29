#!/usr/bin/python3
"""defines a function that prints first name and last name"""

def say_my_name(first_name, last_name=""):
    """prints first name and last name with the input my name is"""

    error_msg = "first_name must be a string or last_name must be a string"

    if not isinstance(first_name, str) or not isintance(last_name, str):
        raise TypeError(error_msg)
    print("My name is", first_name, last_name)
