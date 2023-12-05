0x0A-python-inheritance
this project covers OOP inheritance
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What is a superclass, baseclass or parentclass
What is a subclass
How to list all attributes and methods of a class or instance
When can an instance have new attributes
How to inherit class from another
How to define a class with multiple base classes
What is the default class every class inherit from
How to override a method or attribute inherited from the base class
Which attributes or methods are available by heritage to subclasses
What is the purpose of inheritance
What are, when and how to use isinstance, issubclass, type and super built-in functions

TASKS

0. Lookup
mandatory
Write a function that returns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module

1. My list
mandatory
Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module

2. Exact same object
mandatory
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module

Same class or inherit from
mandatory
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module

4. Only sub class of
mandatory
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
You are not allowed to import any module

5. Geometry module
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an empty class BaseGeometry.

You are not allowed to import any module

6. Improve Geometry
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module

7. Integer validator
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module

8. Rectangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator

9. Full rectangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
