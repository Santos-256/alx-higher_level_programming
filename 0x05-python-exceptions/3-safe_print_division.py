#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        safe_div = a / b
    except (ZeroDivisionError):
        safe_div = None
    finally:
        print("Inside result: {}".format(safe_div))
        return safe_div
