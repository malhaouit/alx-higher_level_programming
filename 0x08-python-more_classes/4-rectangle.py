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
        This method (property) sets the width and
        handles the TypeError and the ValueError.

        args:
            value: the width of the square

        Returns:
            Nothing
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
        This method (property) sets the height and
        handles the TypeError and the ValueError.

        args:
            value (int): the height of the square

        Returns:
            Nothing
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__width != 0 and self.__height != 0:
            return (self.__width + self.__height) * 2

        return 0

    def __str__(self):
        """ Returns the character # """
        string = ""

        if self.__height == 0 or self.__width == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'

        return string

    def __repr__(self):
        """ Returns  a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
