#!/usr/bin/python3
"""
Adds two integers or floats.
"""

def add_integer(a, b=98):
    """Adds two integers or floats."""
    # Check first number
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check second number
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle float overflow (inf, -inf, NaN)
    if a != a or a in (float('inf'), float('-inf')):
        raise TypeError("a must be an integer")
    if b != b or b in (float('inf'), float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
