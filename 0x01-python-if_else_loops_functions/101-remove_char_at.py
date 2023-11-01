#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = str
    if n < 0 or n > len(str):
        return str

    if n == 0:
        str_copy = str[1:]
    elif n == len(str):
        str_copy = str[:n]
    else:
        str_copy = str[:n] + str[n+1:]
    return str_copy
