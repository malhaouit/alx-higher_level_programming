#!/usr/bin/python3
""" This module define one function, no module imported """


def lookup(obj):
    """
    Lists all available attributes and methods of an objet

    Args:
        obj (object): Object type

    Returns: list of members
    """
    return dir(obj)
