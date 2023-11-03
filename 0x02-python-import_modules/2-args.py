#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_of_args = len(sys.argv) - 1

    if num_of_args == 0:
        print("{:d} arguments.".format(num_of_args))
    elif num_of_args == 1:
        print("{:d} argument:".format(num_of_args))
        print("{:d}: {:s}".format(num_of_args, sys.argv[num_of_args]))
    else:
        print("{:d} arguments:".format(num_of_args))
        for i in range(1, num_of_args + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
