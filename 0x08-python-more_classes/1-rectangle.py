#!/usr/bin/python3
"""
Rectangle Module !
"""


class Rectangle:
    """
    Rectangle class !
    """
    def __init__(self, width=0, height=0):
        """ initiate a Rectangle

        Keywords Arguments:
            width {int} --  [width of rectangle]
            height {int} --  [height of rectangle]
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter

        Returns:
            [int] -- [returns the width]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter

        Arguments:
            value {[int]} -- [the value of width]

        Raises:
        TypeError: [if value is not an int]
        ValueError: [if value is negative]
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter

        Returns:
            [int] -- [returns the height]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter

        Arguments:
            value {[int]} -- [the value of height]

        Raises:
        TypeError: [if value is not an int]
        ValueError: [if value is negative]
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
