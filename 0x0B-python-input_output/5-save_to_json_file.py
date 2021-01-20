#!/usr/bin/python3
""" function that writes an Object to a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file

    Arguments:
        my_obj {[object]} -- [JSON object]
        filename {[str]} -- [name of file]

    Returns:
        {txt} -- {text file]
    """
    with open(filename, mode="w") as outfile:
        return json.dump(my_obj, outfile)
