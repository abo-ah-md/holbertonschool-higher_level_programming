#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = None
        result = a/b
    except(ValueError,TypeError,ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(result))
        return result
