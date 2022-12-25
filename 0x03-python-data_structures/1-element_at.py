#!/usr/bin/python3
# 1-element_at.py

""" Description of the prototype"""

def element_at(my_list, idx):
	"""Definition of args and value"""
    if idx < 0:
        return None
    else if idx > len(my_list):
        return None
    else:
	return my_list[idx]
	""" 	This is going to return the element of index	
	Args:
	my_list: is the list name
	idx: is the index number
	"""
