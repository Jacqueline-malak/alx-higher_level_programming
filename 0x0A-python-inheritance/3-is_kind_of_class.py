#!/usr/bin/python3
"""Module: is_kind_of_class.
Check if the object is an instance of, or if the object is an instance of a class that inherited from.

Returns True if it is an instance of a class.
Otherwise false
"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of a_class or a class inherited from a_class.

    Args:
        - obj: This is the object to look out for
        - a_class: This is the class that we are verifying the instace of
    Returns True if the object is an instance of a_class or a class inherited from a_class.
    Otherwise return False
    """

    return isinstance(obj, a_class)
