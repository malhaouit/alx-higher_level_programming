#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        uniques = set()
        for num in my_list:
            uniques.add(num)
        
        result = 0
        for element in uniques:
            result += element
        return result
