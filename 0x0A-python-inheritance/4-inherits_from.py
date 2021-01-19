#!/usr/bin/python3
""" check if object inherited directly or not from a class """


def inherits_from(obj, a_class):
    """ inherits_from definition

    Arguments:
        obj {[object]} -- [the object to check]
        a_class {[class]} -- [the class]

    Returns:
        [bool] -- [True if inherited directly, false if not]
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
