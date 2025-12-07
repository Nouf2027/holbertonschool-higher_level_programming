#!/usr/bin/python3
def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = result.split("\n")
    for line in lines:
        print(line.strip(), end="")
        if line != lines[-1]:
            print()
