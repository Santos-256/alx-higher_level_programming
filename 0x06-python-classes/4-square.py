#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.


        Args:
            size (int): The size of the new square.
        """
        self.size = size

    def get_size(self):
        """Get the current size of the square"""
        return self.__size

    size = property(get_size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the actual area of a square."""
        return self.__size * self.__size
