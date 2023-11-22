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
        self.size(size)

    def area(self):
        """
        calculate the area of the square
        return: the area calculated
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        gets the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the value of size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
