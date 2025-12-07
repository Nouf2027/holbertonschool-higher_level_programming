#!/usr/bin/python3
"""
Adds two integers.
"""

def add_integer(a, b=98):
    """Adds two integers or floats."""
    
    # Detect float overflow (1.0e309 → inf)
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    # Check a type
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check b type
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
