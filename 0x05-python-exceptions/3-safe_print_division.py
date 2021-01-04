#!/usr/bin/python3
def safe_print_division(a, b):
    div_int = 0
    try:
        div_int = a / b
    except ZeroDivisionError:
        div_int = None
    finally:
        print("Inside result: {}".format(div_int))
    return div_int
