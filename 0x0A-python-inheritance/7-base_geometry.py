#!/usr/bin/python3
""" This module based on the previous module 6-base_geometry.py
Addition of more exceptions handling, and no module imported """


class BaseGeometry:
    """ The class BaseGeometry covers different Exception handling """

    def area(self):
        """ Raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Handles TypeError and ValueError exceptions

        Args:
            name (string): string name
            value (int): integer

        Returns: Nothing
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
