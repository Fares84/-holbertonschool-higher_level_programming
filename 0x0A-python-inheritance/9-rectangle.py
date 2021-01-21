#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectange class
    Arguments:
    BaseGeometry {[BaseGeometry]} -- [inherits from BaseGeomtry]
    """

    def __init__(self, width, height):
        """
        Constructor
        Rectanle definition
        Arguments:
            width {[int]} -- [width of rectanle]
            height {[int]} -- [height of rectanle]
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area defintion

        Returns:
            [int] -- [area of rectangle]
        """
        return self.__height * self.__width

    def __str__(self):
        """ str definition

        Return:
            [str] -- [prints the rectangle]
        """
        return "[Rectangle]" + str(self.__width) + "/" + str(self.__height)
