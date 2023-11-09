#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    numerator = 0
    denominator = 0
    result = 0
    for my_tuple in my_list:
        numerator += my_tuple[0] * my_tuple[1]
        numerator = float(numerator)
        denominator += my_tuple[1]
    if denominator != 0:
        return numerator / denominator
