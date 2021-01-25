#!/usr/bin/python3
""" Rectangle definition """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherited from Base

    Args:
        Base ([class]): [Base class that rectangle inherited from]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ defining rectangle

        Args:
        width ([int]): width of rectangle
        height ([int]): height of rectangle
        x (int) : x coordinates (defaults to 0)
        y (int) : y coordinates (defaults to 0)
        id (int): id of rectangle (default to None)
        """
        super().__init__(id)  # call superclass with id __init__Base
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter definition

        returns:
            [int] -- return the rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value{[int]} -- the value of width
        Raises:
            TypeError: if value is not an int
            ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter definition

        returns:
            [int] -- return the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
        Args:
            value{[int]} -- the value of height
        Raises:
            TypeError: if value is not an int
            ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter definition

        returns:
            [int]: x coordinates
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter
        Args:
            value{[int]} -- value assigned to x
        Raises:
            TypeError: if value is not an int
            ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter definition

        returns:
            [int]: y coordinates
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter
        Args:
            value{[int]} -- value assigned to y
        Raises:
            TypeError: if value is not an int
            ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area of Rectangle definition
        returns:
            [int] -- return the area of rectangle
        """
        return self.width * self.height

    def display(self):
        """ prints in the stdout the rectangle instance with #

        returns:
        [str] -- prints the rectangle in #
        """
        for x in range(self.__x):
            print()
        for x in range(self.__height):
            for x in range(self.__y):
                print(" ", end="")
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ str method representation

        returns:
            [str]: update the str method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                    self.width, self.height)

    def update(self, *args, **kwargs):
        """ updated class rectangle """
        attr = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        if not args and kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
