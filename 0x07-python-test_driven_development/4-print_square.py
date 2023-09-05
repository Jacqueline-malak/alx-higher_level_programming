#!/usr/bin/python3
"""
Module print_square
prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #
    size is the len(size)
    size must be an integer or returns an error
    size must not be less than 0 or return an error
    size must not be a float or return an error
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
        
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
