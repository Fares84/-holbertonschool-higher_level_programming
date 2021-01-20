#!/usr/bin/python3
""" function that reads a text file """


def read_file(filename=""):
    """ read_file function

    Keyword Arguments:
        filename {str} -- [the name of the file to read]
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read())
