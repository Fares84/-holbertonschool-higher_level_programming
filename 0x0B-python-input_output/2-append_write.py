#!/usr/bin/python3
""" function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ append_write

    Keyword Arguments:
        filename {str} -- [the name of file]
        text {str} -- [the text to be appended]
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
