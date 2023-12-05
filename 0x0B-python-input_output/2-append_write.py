#!/usr/bin/python3
""" This module covering one function, and no extra module imported """


def append_write(filename="", text=""):
    """ Appends a text to the file """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
