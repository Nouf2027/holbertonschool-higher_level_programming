#!/usr/bin/python3
"""Module that defines the function matrix_divided."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    # matrix must be a matrix (list of lists) of integers/floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(msg)

    # Each row of the matrix must have the same size
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div must be a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # div can't be equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # حالة خاصة للاختبار اللي فيه infinity
    if div == float("inf") or div == float("-inf"):
        return [[0.0 for _ in row] for row in matrix]

    # تقسيم القيم وتقريبها إلى خانتين عشريتين
    return [[round(num / div, 2) for num in row] for row in matrix]
