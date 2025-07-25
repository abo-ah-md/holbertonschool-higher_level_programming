#!/usr/bin/python3
"""
this module use the function text_indentation
to prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """print string with 2lines after ., ? and :"""
    n_line_char = [".", "?", ":"]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in n_line_char:
            print(f"{i}", end="\n\n")
        else:
            print(f"{i}", end="")
