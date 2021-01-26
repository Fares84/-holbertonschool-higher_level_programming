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
        super().__init__(size, size, x, y, id)

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
                                                 self.height)

    def update(self, *args, **kwargs):
        """ update method
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 1:
                    self.x = args[i]
                if i == 1:
                    self.y = args[i]
        if not args and kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dict method

        returns:
            [dict]: dict representation of square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
