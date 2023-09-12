#!/usr/bin/python3
"""Module: 2-is_same_class.
Check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Function that check if an object is exactly an instance of a specified class.

    Args:
        - obj: This is the object to look out for
        - a_class: This is the class that we are verifying the instace of
        
    Returns True if the object is exactly an instance of a specified class.
    Otherwise return False
    """

    return True if type(obj) is a_class else False
