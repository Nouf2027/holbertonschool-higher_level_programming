#!/usr/bin/python3
"""
Defines a class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending order)
        """
        print(sorted(self))
