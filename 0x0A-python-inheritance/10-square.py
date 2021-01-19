#!/usr/bin/python3
""" Square definition """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class

    Arguments:
    Rectangle {[Rectangle]} -- [inherited from Rectangle class]
    """
    def __init__(self, size):
        """ square initialized

        Arguments:
            size {[int]} -- [size of square]
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
