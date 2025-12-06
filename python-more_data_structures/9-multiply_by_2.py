#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}                     # create new empty dictionary
    for key, value in a_dictionary.items():   # loop on all key/value pairs
        new_dict[key] = value * 2     # same key, value * 2
    return new_dict                   # return the new dictionary
