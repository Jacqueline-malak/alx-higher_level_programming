#!/usr/bin/python3
"""
Module: 1-my_list
This is a class that inherits from list
It prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    A function that print the list in sorted ascending order
    """
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
