#!/usr/bin/python3
"""
This module contains mathematic function add_integer.
"""


def add_integer(a, b=98):
    """
    This function add_integer(a, b=98) adds two integers.

    args:
    a (int) or (float): The argument must be integer or float
    b (int) or (float): The argument must be integer or float

    Returns:
    The addition of a and b (The result must be an integer)
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
