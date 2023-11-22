#!/usr/bin/python3
""" Square class, no module imported """


class Square:
    """ Square class that defines a square """

    def __init__(self, size=0):
        self.__size = size
    """ value instantiation of size attribute """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
