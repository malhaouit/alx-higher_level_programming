#!/usr/bin/python3
"""
This module includes a Square class that inherits from
a super class: Rectangle class (look at file rectangle.py).

Current file: square.py
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the attributes: size, x, y and id.
        This class constructor (__init__) use the logic of __init__
        of the Rectangle class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Formats a Square object to a human readable text """
        id = self.id
        x = self.x
        y = self.y
        size = self.width

        return '[Square] ({}) {}/{} - {}'.format(id, x, y, size)

    @property
    def size(self):
        """ Gets the Square size """
        return self.width

    @size.setter
    def size(self, size):
        """ Checks exceptions and sets the value of Square size
        if no exception occured """
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        elif size <= 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Updates the Square attributes """
        attributes = ['id', 'size', 'x', 'y']

        if args and len(args) > 0:
            for index, value in enumerate(args):
                if index < len(args):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        to_dict = {}
        to_dict['id'] = self.id
        to_dict['x'] = self.x
        to_dict['size'] = self.size
        to_dict['y'] = self.y
        return to_dict
