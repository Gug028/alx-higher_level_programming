#!/usr/bin/python3

"""
Rectangle class.
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Definition """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width"""
        return self._width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Height"""
        return self._height

    @height.setter
    def height(self, value):
        """Height stter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
