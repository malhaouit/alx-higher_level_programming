#!/usr/bi/python3
def uppercase(str):
    uppercase = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            uppercase += chr(ord(str[i]) - 32)
        else:
            uppercase += str[i]
    print("{}".format(uppercase))
