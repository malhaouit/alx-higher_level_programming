#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result:", end=" ")
        result = None
    else:
        print("Inside result:", end=" ")
        return result
    finally:
        print("{}".format(result))
