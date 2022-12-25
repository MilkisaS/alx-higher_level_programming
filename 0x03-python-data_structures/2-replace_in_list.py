#!/usr/bin/python3
# 2-replace_in_list.py

"""This is the prototype"""

def replace_in_list(my_list, idx, element):
    """Is used to replace an element at specific place"""
    if idx >= 0 or idx < len(my_list):
        my_list[idx] = element
    return (my_list)
