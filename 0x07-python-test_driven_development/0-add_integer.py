#!/usr/bin/python3
"""
an addition function: add_integer():
>>> add_integer(1, 1)
2
"""


def add_integer(a, b=98):
    """
    Arguments:
        a {[int or float]} -- [first int to add]

    keyword Arguments:
        b {[int or float]} -- [second int to add] (default: 98)

    Raises:
        TypeError: [if a is not int or float]
        TypeError: [if b is not int or float]

    Returns:
        [int] -- [a + b]
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
