#!/usr/bin/python3
"""
Rectangle Module !
"""


class Rectangle:
    """
    Rectangle class !
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initiate a Rectangle

        Keywords Arguments:
            width {int} --  [width of rectangle]
            height {int} --  [height of rectangle]
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Area of Rectangle

        returns:
            [int] -- [returns the area of rectangle]
        """
        return self.width * self.height

    def perimeter(self):
        """ Perimeter of Rectangle

        returns:
            [int] -- [returns the perimeter of rectangle]
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        srec = ""
        if self.__height == 0 or self.__width == 0:
            srec = ""
        for x in range(self.__height):
            for y in range(self.__width):
                srec += str(self.print_symbol)
            srec += "\n"
        return srec[:-1]

    def __repr__(self):
        """ rectangle's representation

        returns:
            [] -- [representation of rectangle]
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        message to display when instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger or equal

        Arguments:
            rect_1 {[Rectangle]} -- [an instance of Rectangle]
            rect_2 {[Rectangle]} -- [an instance of Rectangle]

        Raises:
            TypeError: [if rect_1 is not an instance of Rectangle]
            TypeError: [if rect_2 is not an instance of Rectangle]

        Returns:
            [Rectangle] -- [returns the biggest rectangle based on the area]
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        square class method

        Keywords Arguments:
            size [int] -- [size of square]

        Returns:
            [Rectangle] -- [an instance of rectangle]
        """
        return cls(size, size)
