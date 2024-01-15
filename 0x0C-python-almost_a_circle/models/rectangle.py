#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class ModifiedRectangle(Base):
    """Represent a rectangle."""

    def __init__(self, modified_width, modified_height, modified_x=0, modified_y=0, modified_id=None):
        """Initialize a new Rectangle.

        Args:
            modified_width (int): The width of the new Rectangle.
            modified_height (int): The height of the new Rectangle.
            modified_x (int): The x coordinate of the new Rectangle.
            modified_y (int): The y coordinate of the new Rectangle.
            modified_id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.modified_width = modified_width
        self.modified_height = modified_height
        self.modified_x = modified_x
        self.modified_y = modified_y
        super().__init__(modified_id)

    @property
    def modified_width(self):
        """Set/get the width of the Rectangle."""
        return self.__modified_width

    @modified_width.setter
    def modified_width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__modified_width = value

    @property
    def modified_height(self):
        """Set/get the height of the Rectangle."""
        return self.__modified_height

    @modified_height.setter
    def modified_height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__modified_height = value

    @property
    def modified_x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__modified_x

    @modified_x.setter
    def modified_x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__modified_x = value

    @property
    def modified_y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__modified_y

    @modified_y.setter
    def modified_y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__modified_y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.modified_width * self.modified_height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.modified_width == 0 or self.modified_height == 0:
            print("")
            return

        [print("") for y in range(self.modified_y)]
        for h in range(self.modified_height):
            [print(" ", end="") for x in range(self.modified_x)]
            [print("#", end="") for w in range(self.modified_width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.modified_width, self.modified_height, self.modified_x, self.modified_y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.modified_width = arg
                elif a == 2:
                    self.modified_height = arg
                elif a == 3:
                    self.modified_x = arg
                elif a == 4:
                    self.modified_y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.modified_width, self.modified_height, self.modified_x, self.modified_y)
                    else:
                        self.id = v
                elif k == "width":
                    self.modified_width = v
                elif k == "height":
                    self.modified_height = v
                elif k == "x":
                    self.modified_x = v
                elif k == "y":
                    self.modified_y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.modified_width,
            "height": self.modified_height,
            "x": self.modified_x,
            "y": self.modified_y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.modified_x, self.modified_y,
                                                       self.modified_width, self.modified_height)
