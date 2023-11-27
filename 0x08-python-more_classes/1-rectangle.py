#!/usr/bin/python3
""" This is a module includes Rectangle class, no module imported """


class Rectangle:
    """
    This is a class: Rectangle
    The class have:
        - __init__ method for attributes initialization
        - Two attributes, width and height
        - Properties that retrieves and sets width and height
    """

    def __init__(self, width=0, height=0):
        """ Define and initialize width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ This method (property) Gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method (property):
            - Principal goal: Sets the width
            - Handles two types of error: TypeError and ValueError
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ This method (property) Gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method (property):
        - Principal goal: Sets the height
        - Handles two types of error: TypeError and ValueError
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
