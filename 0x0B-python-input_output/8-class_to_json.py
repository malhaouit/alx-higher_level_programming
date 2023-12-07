#!/bin/usr/python3
""" Returns the dictionary description for JSON serialization of an object """


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object
    """
    return obj.__dict__
