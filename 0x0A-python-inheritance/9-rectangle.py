#!/usr/bin/python3
"""Module: 8-rectangle
This is a rectangle class that inherit the BaseGeometry from the BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a rectangle class
    It has the following private attribute:
        width = __width
        height = __height
    It inherits the integer validator from the BaseGeometry class
    """

    def __init__(self, width, height):
        """Validates the following attributes:
            - width
            - height
        """


        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a format string of the attribute width and height"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Returns the area of both attribute"""

        return self.__width * self.__height
