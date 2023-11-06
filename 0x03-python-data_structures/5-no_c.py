#!/usr/bin/python3

def no_c(my_string):
    string_list = []
    new_list = []
    new_string = ""

    for i in range(len(my_string)):
        string_list.append(my_string[i])

    new_list = [char for char in string_list if char != 'C' and char != 'c']

    for i in range(len(new_list)):
        new_string += new_list[i]

    return new_string
