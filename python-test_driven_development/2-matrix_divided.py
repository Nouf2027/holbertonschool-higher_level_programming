#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div"""
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check elements of matrix
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check same row size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division
    return [[round(num / div, 2) for num in row] for row in matrix]
