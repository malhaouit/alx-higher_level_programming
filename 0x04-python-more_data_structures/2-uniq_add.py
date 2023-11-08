#!/usr/bin/python3

def uniq_add(my_list=[]):
        uniques = set(my_list)
        result = 0

        for element in uniques:
            result += element
        return result
