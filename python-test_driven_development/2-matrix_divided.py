#!/usr/bin/python3
"""
This module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    
    # Error messages
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"
    div_type_err = "div must be a number"
    div_zero_err = "division by zero"

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError(div_type_err)
    
    if div == 0:
        raise ZeroDivisionError(div_zero_err)

    # Validate matrix structure and content
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(type_err)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(type_err)
        
        # Check if row size matches the first row
        if len(row) != len(matrix[0]):
            raise TypeError(size_err)
        
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(type_err)

    # Perform division and return new matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
