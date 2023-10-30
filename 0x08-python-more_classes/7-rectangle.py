#!/usr/bin/python3


class Rectangle:
    """
    Class that defines a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with a given width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using print_symbol.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return (symbol * self.width + "\n") * self.height

    def __repr__(self):
        """
        Returns a string representation of the rectangle to recreate a new instance.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
