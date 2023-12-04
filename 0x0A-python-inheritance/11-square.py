#!/usr/bin/python3
""" This module based on the previous module 9-base_geometry.py
Additions: Implementation of erea method for Square class and string formatting
No module imported """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class represents a Square that inherits from Rectangle class """
    def __init__(self, size):
        """ Initializes the attribute size after validating its value.
        The Square class inherits the __init__ method of the Rectangle class
        to initialize the size attribute.

        Args:
            size (int): the size of the square

        Returns: Nothing
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ Returns the erea of the square """
        return self.__size ** 2

    def __str__(self):
        """ Formats the string to: [Rectangle] <size>/<size> """
        return return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
