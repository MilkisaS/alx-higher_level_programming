#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Returns copy of replaced element wihtout affecting other elements"""

    if idx < 0 or idx >= len(my_list):
        return (my_list)
    copy = [ x for x in my_list]
    copy[idx] = element
    return (copy)
