#!/usr/bin/python3
""" This module covers one function that converts an object to a JSON string
representation """

import json


def to_json_string(my_obj):
    """ Converts an object to its JSON string representation

    Args:
        my_obj (object): The object to convert

    Returns:
        A JSON string representation of `my_obj`
    """
    return json.dumps(my_obj)
