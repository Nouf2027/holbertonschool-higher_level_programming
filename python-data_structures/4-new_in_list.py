#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element at a specific index in a copy of the list"""

    new_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element

    return new_list
