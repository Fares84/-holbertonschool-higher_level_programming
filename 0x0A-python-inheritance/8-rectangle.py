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
