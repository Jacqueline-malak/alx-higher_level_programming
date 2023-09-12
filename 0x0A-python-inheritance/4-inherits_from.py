#!/usr/bin/python3
"""Module 4-inherits_from.py
Checking if the object is an instance from a class int or from a class object
"""


def inherits_from(obj, a_class):
    """Checking if the object is an instance of a class inherited from a class
    Args:
        obj: - this is the object to look out
        a_class: - class to evaluate
    """

    return isinstance(obj, a_class) and type(obj) != a_class
