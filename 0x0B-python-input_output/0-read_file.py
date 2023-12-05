#!/usr/bin/python3
""" This module cover one function, and no extra module is imported """


def read_file(filename=""):
    """ Reads a text file """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end="")
