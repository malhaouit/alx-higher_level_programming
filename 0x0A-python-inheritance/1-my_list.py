#!/usr/bin/python3
""" This module cover the concept of inheritance """


class MyList(list):
    """ This class inherits from the built-in list """

    def print_sorted(self):
        """
        Prints a sorted list

        Args: no arguments

        Returns: nothing
        """
        print(sorted(self))
