#!/usr/bin/python3
""" This module includes one function that creates an Object
from a “JSON file” """
import json


def load_from_json_file(filename):
    """ Creates an object from a “JSON file”

    Args:
        filename: the JSON file

    Returns:
        the object created from the JSON file (filename) """
    with open(filename, 'r') as f:
        return json.load(f)
