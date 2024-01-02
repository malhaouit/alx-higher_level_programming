#!/usr/bin/python3
"""
This module includes a class that inherits from
a super class: class Base (look at file base.py).

Current file: rectangle.py
"""
from .base import Base


class Rectangle(Base):
    """ This class Rectangle represent a rectangle shape.
    It includes class Constructor (__init__), getters and setters. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instance attributes (width, height, x, y, id).
        The id attribute is inherited from the Base class. """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Gets the rectangle width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Checks exceptions and sets the value of rectangle width
        if no exception occured """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """ Gets the rectangle height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Checks exceptions and sets the value of rectangle height
        if no exception occured """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """ Gets x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Checks exceptions and sets the value of x
        if no exception occured"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """ Gets y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Checks exceptions and sets the value of y
        if no excetpion occured """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ Returns the erea value of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ Displays a square using the character `#` at a specific
        position (x,y) """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ Formatting the Rectangle object text """
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height

        return '[Rectangle] ({}) {}/{} - {}/{}'.format(id, x, y, width, height)

    def update(self, *args, **kwargs):
        """ Updates the attributes of the Rectangle instance """
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args and len(args) > 0:
            for index, value in enumerate(args):
                if index < len(args):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        to_dict = {}
        to_dict['x'] = self.x
        to_dict['y'] = self.y
        to_dict['id'] = self.id
        to_dict['height'] = self.height
        to_dict['width'] = self.width
        return to_dict
