#!/usr/bin/python3
"""Defines a clas-checking function"""

def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
