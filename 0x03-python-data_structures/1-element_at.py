#!/usr/bin/python3
# 1-element_at.py

""" Description of the prototype"""

def element_at(my_list, idx):

    """Is used to retrieve element from a list"""

    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return my_list[idx]
