#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'"""

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
            print()
            result = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    if result.strip() != "":
        print(result.strip(), end="")
