#!/usr/bin/python3
"""define the Rectangle class"""

class Rectangle:

    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): the width of rectangle
            height (int): the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle = []
        for i in range(self.__height):
            for n in range(self.__width):
                rectangle.append('#')
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")