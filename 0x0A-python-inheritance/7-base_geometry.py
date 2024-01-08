#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""

class BaseGeometry:

    def area(self):
        """Un implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise valueError("{} must be greater than 0".format(name))
