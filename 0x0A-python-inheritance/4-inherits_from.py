#!/usr/bin/python3
def inherits_from(obj, a_class):
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
