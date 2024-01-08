#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
       self.integer_validator("size", size)
       supper().__init__(size, size)
       self.__size = size
