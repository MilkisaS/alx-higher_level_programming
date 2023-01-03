#!/usr/bin/python3
def magic_string():
    """Returns string School n times"""
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("School, " * (magic_string.n - 1) + "School")
