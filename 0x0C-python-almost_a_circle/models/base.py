#!/usr/bin/python3
""" Base definition """
from os import path


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base initialization

        Arguments:
            id ([int], optional): [the id]. Defaults to None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
