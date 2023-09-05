#!/usr/bin/python3
"""
Module say_my_name
Prints out first name and last name
"""
    
    def say_my_name(first_name, last_name=""):
        """
        prints out first name ans las name 
        first name and last name must be in tye of string 
        or error if not string """

        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
         if type(last_name) is not str:
            raise TypeError("last_name must be a string")
         
        print("My name is {} {}".format(first_name, last_name))
