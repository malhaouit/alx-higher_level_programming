#!/usr/bin/python3
""" This module covers on function that coverts a JSON string
into a Python data structure """

import json


def from_json_string(my_str):
    """ Converts a JSON string into a Python object

    Args:
        my_str (JSON string): The JSON string to convert

    Returns:
        The Python data structure of `my_str` """
    return json.loads(my_str)
