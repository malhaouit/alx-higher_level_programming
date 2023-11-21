#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        i = 0
        while i < x:
            element = my_list[i]
            if type(element) == int:
                print("{:d}".format(element), end="")
                count += 1
            i += 1
    except (ValueError):
        pass

    print()
    return count
