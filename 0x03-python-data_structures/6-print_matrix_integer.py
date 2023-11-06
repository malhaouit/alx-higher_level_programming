#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print("{}".format(matrix[i][j]), end=" ")
        print()
        if i * j == (len(matrix[0]) - 1) * (len(matrix) - 1):
            break
    else:
        print()
