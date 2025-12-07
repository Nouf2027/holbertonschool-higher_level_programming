#!/usr/bin/python3
"""
Module that provides add_integer function.
"""

def add_integer(a, b=98):
    """Adds two integers."""
    # Check types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check overflow (Holberton test)
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
