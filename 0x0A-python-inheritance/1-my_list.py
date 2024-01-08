#!/usr/bin/python3
"""Defines class MyList."""

class MyList(list):
    """Implements sorted printing for the built-in list class"""


    def print_sorted(self):
        """prints a list in sorted ascending order"""
        print(sorted(self))
