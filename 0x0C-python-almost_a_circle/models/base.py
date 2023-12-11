#!/usr/bin/python3
"""
This module has a class Base that will be the “base”
of all other classes in this project

Current file: base.py
"""


class Base:
    """ The “base” class of all other classes in this project """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instance attributes

        Args:
            id (int): the id attribute

        Returns:
            nothing """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
