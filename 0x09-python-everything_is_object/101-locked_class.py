#!/usr/bin/python3
""" This module cover a Locked Class, no module imported """


class LockedClass:
    """
    This a class with no class or object attribute and prevents any creation
    of a new instance attributes, except if the new instance attribute
    is called `first_name`
    """

    __slots__ = 'first_name',
