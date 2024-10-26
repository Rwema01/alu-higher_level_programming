#!/usr/bin/python3
"""Inherits BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle."""

    def __init__(self, size):
        """Initializes data."""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Area of Square."""
        return self.__size ** 2


if __name__ == "__main__":
    s = Square(5)
    print(s)              # Expected output: [Square] 5/5
    print(s.area())       # Expected output: 25
