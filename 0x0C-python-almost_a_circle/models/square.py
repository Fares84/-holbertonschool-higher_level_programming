#!/usr/bin/python3
""" class square definition """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class

    Args:
        Rectangle ([class]): class that square inherits from
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square initialization

        Args:
            size ([int]): size of square
            x (int): x coordinates
            y (int): y coordinates
            id ([type], optional): square id
        """
        super().init(size, size, x, y, id)

        @property
        def size(self):
            """ size getter

            returns:
                [int]: size of square
            """
            return self.width

        @size.setter
        def size(self, value):
            """ size setter

            Args:
                value ([int]): value assigned to size
            """
            self.width = value
            self.height = value

        def __str__(self):
            """ str method

            returns:
                [str]: str representation of square
            """
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                     self.size)
