#!/usr/bin/python3
"""Module that defines the text_indentation function."""


def text_indentation(text):
    """Print a text with 2 new lines after each of '.', '?' and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in ".?:":
                       result = result.rstrip()
            print(result)
            print()    

            result = ""
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    if result.strip() != "":
        print(result.strip(), end="")
