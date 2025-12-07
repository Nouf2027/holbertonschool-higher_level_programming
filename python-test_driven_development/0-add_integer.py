#!/usr/bin/python3
"""
Adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    a and b must be integers or floats, otherwise TypeError is raised.
    Floats are casted to integers before addition.
    """
    # Check invalid float values (NaN, inf)
    if isinstance(a, float):
        if a != a or a == float('inf') or a == -float('inf'):
            raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b != b or b == float('inf') or b == -float('inf'):
            raise TypeError("b must be an integer")

    # Check type validity
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
