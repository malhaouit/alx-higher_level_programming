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
        self.__size = size

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Prints the square with character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
