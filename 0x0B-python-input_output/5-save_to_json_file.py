#!/usr/bin/python3
"""" This module includes one function that uses the json.dump() method
to convert a Python object into a JSON string and write it to a file """

import json


def save_to_json_file(my_obj, filename):
    """ Converts a Python object into a JSON string and write it to
    the file filename

    Args:
        my_obj (object): the object to convert
        filename (file): the file where to write and save the
        converted object

    Returns:
        Nothing """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
