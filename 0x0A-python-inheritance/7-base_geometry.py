#!/usr/bin/python3
"""
Module: 7-base_geometry
Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates  the value
"""


class BaseGeometry:
    """
    Class with public instance methods.
    It raises an Exception with the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
