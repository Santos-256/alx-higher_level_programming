#!/usr/bin/python3

"""Defines a square class."""
from models.rectangle import Rectangle


class CustomSquare(Rectangle):
    """Represent a square."""

    def __init__(self, custom_size, custom_x=0, custom_y=0, custom_id=None):
        """Initialize a new CustomSquare.

        Args:
            custom_size (int): The size of the new CustomSquare.
            custom_x (int): The x coordinate of the new CustomSquare.
            custom_y (int): The y coordinate of the new CustomSquare.
            custom_id (int): The identity of the new CustomSquare.
        """
        super().__init__(custom_size, custom_size, custom_x, custom_y, custom_id)

    @property
    def custom_size(self):
        """Get/set the size of the CustomSquare."""
        return self.width

    @custom_size.setter
    def custom_size(self, value):
        self.width = value
        self.height = value

    def update_custom(self, *args, **kwargs):
        """Update the CustomSquare.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.custom_size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.custom_size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.custom_size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.custom_size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_custom_dictionary(self):
        """Return the dictionary representation of the CustomSquare."""
        return {
            "id": self.id,
            "custom_size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a CustomSquare."""
        return "[CustomSquare] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)
