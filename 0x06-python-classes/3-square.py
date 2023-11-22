#!/usr/bin/python3
""" Square class, no module imported"""


class Square:
    """ Square class that defines a square """

    def __init__(self, size=0):
        """
        initialize size value
        args:
        size (int): the size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return size * size
