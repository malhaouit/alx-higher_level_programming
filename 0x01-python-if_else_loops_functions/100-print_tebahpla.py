#!/usr/bin/python3
for ascii_value in reversed(range(97, 123)):
    if ascii_value % 2 == 0:
        pass
    else:
        ascii_value = ascii_value - 32
    print("{}".format(chr(ascii_value)), end="")
