#!/usr/bin/python3
""" This module contains a class with three functions, no module imported """


class MyInt(int):
    """  MyInt class inherits from int class """

    def __init__(self, obj):
        """ Initializes obj attribute

        Args:
            obj (object): it can any type

        Returns: Nothing
        """
        self.obj = obj

    def __eq__(self, obj):
        """ Invert the operator `==` """
        return super().__ne__(obj)

    def __ne__(self, obj):
        """" Invert the operator `!=` """
        return super().__eq__(obj)
