#!/usr/ba in/python3
"""
This module includes a Square class that inherits from
a super class: Rectangle class (look at file rectangle.py).

Current file: square.py
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Formats a Square object to a human readable text """
        id = self.id
        x = self.x
        y = self.y
        size = self.width

        return '[Square] ({}) {}/{} - {}'.format(id, x, y, size)
