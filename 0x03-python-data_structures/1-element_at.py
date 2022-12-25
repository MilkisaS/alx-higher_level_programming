#!/usr/bin/python3
# 1-element_at.py

""" Description of the prototype"""

def element_at(my_list, idx):
    """Definition of args and value"""
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    else:
	return my_list[idx]	
    
    """ This is the description of elements used

    Args:
    my_list: The name of the list
    idx: The index number to retrieve the element
    """
