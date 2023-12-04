#!/usr/bin/python3
""" This module has one function """


def is_same_class(obj, a_class):
    """
    Checks if an object is `exactly` an instance of the specified class

    Args:
        obj (object): it can be any type of object
        a_class (class): the specified class

    Returns: True if the object is `exactly ` an instance of the class
    or False if not
    """
    return (type(obj) is a_class)
