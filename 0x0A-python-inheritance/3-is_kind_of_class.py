#!/usr/bin/python3
""" This module has one function, no module imported """


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Args:
        obj (object): it can be any type of object
        a_class (class): the specified class

    Returns: True or False
    """
    return isinstance(obj, a_class)
