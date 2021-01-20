#!/usr/bin/python3
""" function that writes str to a text file and returns the number of char """


def write_file(filename="", text=""):
    """ write_file

    Keyword Arguments:
        filename {str} -- [name of the file]
        text {str} -- [description]

    Returns:
        [type] -- [descriptio]
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
