#!/usr/bin/python3

from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

if int(argv[1]) < 4:
    print('N must be at least 4')
    exit(1)
