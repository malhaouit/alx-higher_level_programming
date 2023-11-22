#!/usr/bin/python3
""" Square class, no module imported """


class Square:
    """ Square class that defines a square """

    def __init__(self, size=0):
        """
        value instantiation of size attribute
        args:
        size (int): size of the square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
