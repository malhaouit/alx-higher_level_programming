#!/usr/bin/python3
""" This module contains simple division operation on a matrix """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number

    args:
        - matrix (list of lists): The matrix containing integers or floats.
        - div (int or float): The number that devide each element
        in the matrix

    Returns:
        A new matrix with elements rounded to 2 decimal places.
    """

    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    new_row = []
    for row in matrix:
        for val in row:
            new_row.append(round(val / div, 2))
        new_matrix.append(new_row)
        new_row = []

    return new_matrix

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
