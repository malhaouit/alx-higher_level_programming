#!/usr/bin/python3
"""
The class Student that defines a student is based on 9-student.py
current file: 10-student.py
functions:
=> __init__
=> def to_json
"""


class Student:
    """ Student class that defines a student """
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

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance.
        Only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved

        Args:
            attrs: only attribute names contained in the list

        Returns:
            a dictionary of retrieved names """

        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
