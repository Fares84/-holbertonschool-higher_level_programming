#!/usr/bin/python3
""" function that returns the dictionary description with simple data
structure for JSON serialization of an object """


def class_to_json(obj):
    """  load_from_json_file

    Arguments:
        filename {[str]} -- [the file name]

    Returns:
        (object) -- [JSON object]
    """
    return obj.__dict__
