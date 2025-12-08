#!/usr/bin/python3
"""A function that prints a text with 2 new lines after '.', '?' and ':'"""


def text_indentation(text):
    """Prints text with two new lines after '.', '?', ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        char = text[i]
        result += char

        if char in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    print(result, end="")
