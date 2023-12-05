#!/usr/bin/python3
""" This module has one function, and no extra module imported """


def write_file(filename="", text=""):
    """ Writes a text into the filename """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
