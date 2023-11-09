#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        roman_numbers_dict = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000
                }
        number = 0
        previous_value = 0
        for letter in reversed(roman_string):
            value = roman_numbers_dict[letter]
            if value < previous_value:
                number -= value
            else:
                number += value
            previous_value = value

        return number
