#!/usr/bin/python3
""" function that returns the JSON representation of an object """
import json


def to_json_string(my_obj):
    """ to_json_string

    Arguments:
        my_obj {[object]} -- [the object get its representation]

    Returns:
        {str}  -- [json reprsentation oj object]
    """
    return json.dumps(my_obj)
