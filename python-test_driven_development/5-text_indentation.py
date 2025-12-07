#!/usr/bin/python3
"""Module that defines the text_indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    result = ""

    while i < len(text):
        char = text[i]
        result += char

        if char in ".?:":
            print(result.strip())
            print()
            result = ""

            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    if result.strip():
        print(result.strip(), end="")
