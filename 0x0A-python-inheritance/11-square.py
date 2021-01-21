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

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
