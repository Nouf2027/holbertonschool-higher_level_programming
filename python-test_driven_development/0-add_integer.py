#!/usr/bin/python3
"""
Adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers or floats and returns an int."""
    # Handle float overflow (1.0e309 → inf / -inf)
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    # Check type of a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check type of b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to int then add
    return int(a) + int(b)
