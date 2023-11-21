#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            result_element = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            result_element = 0
            print("wrong type")
        except ZeroDivisionError:
            result_element = 0
            print("division by 0")
        except IndexError:
            result_element = 0
            print("out of range")
        finally:
            result_list.append(result_element)

    return result_list
