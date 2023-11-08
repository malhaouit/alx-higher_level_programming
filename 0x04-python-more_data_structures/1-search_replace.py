#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        new_list = my_list.copy()

        for element in new_list:
            if element == search:
                index = new_list.index(element)
                new_list[index] = replace
        return new_list
