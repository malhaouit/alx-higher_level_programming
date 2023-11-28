#!/usr/bin/python3
"""
This is a module conatains one function that print a square
No mudule imported
"""


def print_square(size):
    """
    Prints a square with character '#'.

    args:
        size (int): The size of the square

    Returns: Nothing
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    elif not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
