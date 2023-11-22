#!/usr/bin/python3
""" Square class, no module imported"""


class Square:
    """ Square class that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize size value
        args:
        size (int): the size of square
        position (tuple): a tuple that represent coordinates
        of a square
        """
        self.__size = size
        self.position = position

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
            return

        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """ gets the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the position """
        if len(value) != 2 or \
                not isinstance(value[0], int) or \
                not isinstance(value[1], int) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple \
                    of 2 positive integers")
        self.__position = value
