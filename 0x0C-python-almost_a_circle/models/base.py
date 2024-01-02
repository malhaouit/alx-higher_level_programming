#!/usr/bin/python3
"""
This module has a class Base that will be the “base”
of all other classes in this project

Current file: base.py
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list of dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
