#!/usr/bin/python3
"""
a text printing function: text_indentetion():
>>> text_indentation(text.   text1)
text.\n\text1
"""


def text_indentation(text):
    """
    Arguments:
       text {[str]} -- ("text must be a string]

    Raises:
        TypeError: [if text given is not str]
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for i in text:
        new_text += i
        if i in ".?:":
            print(new_text.lstrip(), end="\n\n")
            new_text = ""
    print(new_text.lstrip(), end="")
