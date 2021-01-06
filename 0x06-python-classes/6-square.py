#!/usr/bin/python3
""" Square Class """


class Square:
    """ class square """

    def __init__(self, size=0, position=(0, 0)):
        """ class constructor """
        self.size = size
        self.position = position

    def area(self):
        """ method area """
        return self.__size ** 2

# get & set size
    @property
    def size(self):
        """ size def """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be >= 0")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

# get & set position
    @property
    def position(self):
        """ position def """
        return self.__position

    @position.setter
    def position(self, value):
        """ position check """
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """ print square in # """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
