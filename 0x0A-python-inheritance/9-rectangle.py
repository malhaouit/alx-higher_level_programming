#!/usr/bin/python3
""" This module based on the previous module 8-base_geometry.py
Additions: Implementation of erea method and write str() function
No module imported """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class represents a Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initializes the attributes width and height after validating their
        types, i.e it checks if they are integers before initializing them

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        Returns: Nothing """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the erea of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Formats the string [Rectangle] <width>/<height> """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
