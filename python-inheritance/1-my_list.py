#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class that can print a sorted version of itself."""

    def print_sorted(self):
        """Print the list, but sorted (ascending), without changing the original."""
        print(sorted(self))
