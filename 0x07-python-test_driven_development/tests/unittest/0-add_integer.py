#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """Addition of integer number

    Raises:
    TypeError: if A and b are not either integer or float

    """
    if (a is None or not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (b is None or not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
