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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Defines and initializes width and height
        Counts the number of instances
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                if isinstance(self.print_symbol, str):
                    string += self.print_symbol
                else:
                    string += str(self.print_symbol)
            if i != self.__height - 1:
                string += '\n'

        return string

    def __repr__(self):
        """ Returns  a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Deletes an instance of rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle
        args:
            rect_1 (Rectangle instance)
            rect_2 (Rectangle instance)
        Returns:
            The biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
