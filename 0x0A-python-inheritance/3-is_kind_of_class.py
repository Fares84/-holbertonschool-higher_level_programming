#!/usr/bin/python3
""" check if object is an instance of a class that inherited
 (directly or indirectly) from the specified class """


def is_kind_of_class(obj, a_class):
    """ inherits_from definition

    Arguments:
        obj {[object]} -- [the object to check]
        a_class {[class]} -- [the class]

    Returns:
        [bool] -- [True if inherited directly, false if not]
    """
    if isinstance(obj, a_class):
        return True
    return False
