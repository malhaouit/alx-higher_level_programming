#!/usr/bin/python3
"""" This module contains a function for printing a string """

def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    args:
        first_name (string): The first name
        last_name (string): The last name

    Returns: Nothing
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
