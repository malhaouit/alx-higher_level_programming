#!/usr/bin/python3
""" This module contains one function, no module imported """


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (object): it can be any object type
        a_class (class): the specified class

    Returns: True or false
    """
    return isinstance(obj, a_class) and (type(obj) is not a_class)
