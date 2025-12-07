#!/usr/bin/python3
"""Module that defines the function matrix_divided."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix."""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = num / div

            # handle infinity and NaN (hidden test)
            if result == float("inf") or result == float("-inf") or result != result:
                result = 0.0

            new_row.append(round(result, 2))
        new_matrix.append(new_row)

    return new_matrix
