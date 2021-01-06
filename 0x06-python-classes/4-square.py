#!/usr/bin/python3
""" Square Class """


class Square:
    """ class square """

    def __init__(self, size=0):
        """ class constructor """
        self.size = size

    def area(self):
        """ method area """
        return self.__size ** 2

    @property
    def size(self):
        """ size def """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
