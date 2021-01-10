#!/usr/bin/python3
"""
a square printing function: print_square():
>>> def print_square(1):
#
"""


def print_square(size):
    """
    Argument:
        size {[int]} -- [size of square]

    Raises:
        TypeError: [if size is not int]
        ValueError: [if size < 0]
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    else:
        for row in range(size):
            print("#" * size)
