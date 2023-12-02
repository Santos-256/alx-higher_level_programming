#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for charactor in my_string:
        if charactor != "c" and charactor != "C":
            new_string += charactor
    return new_string
