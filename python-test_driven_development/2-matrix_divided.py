#!/usr/bin/python3
"""Module that defines the function matrix_divided."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list of lists of int/float): matrix to be divided.
        div (int or float): number to divide by.

    Returns:
        list of lists of float: new matrix with values rounded to 2 decimals.

    Raises:
        TypeError: if matrix is not a matrix (list of lists) of ints/floats.
        TypeError: if each row of the matrix is not the same size.
        TypeError: if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    # check matrix structure and element types
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # check all rows same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # check div is number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # return new matrix with numbers divided and rounded to 2 decimals
    return [[round(num / div, 2) for num in row] for row in matrix]
