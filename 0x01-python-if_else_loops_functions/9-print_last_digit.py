#!/usr/bin/python3
def print_last_digit(number):
   # for last_digit in number:
        if last_digit < 0:
            last_digit = number % -10
        elif last_digit > 0:
            last_digit = number % 10
        print("{:d}".format(last_digit), end='')
        return last_digit
