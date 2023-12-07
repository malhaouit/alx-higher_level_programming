#!/usr/bin/python3
"""
file: 9-student.py
functions:
=> __init__
=> def to_json(self)
"""


class Student:
    """ Student class that defines the full_name and the age of
    a Student instance """
    def __init__(self, first_name, last_name, age):
        """ Initializes the instance attributes.

        Args:
            first_name (string): the first name.
            last_name (string): the last name.
            age (int): the age.

        Returns:
            nothing """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        return self.__dict__
