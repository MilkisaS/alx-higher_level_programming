#!/usr/bin/python3

#0-print_list_integer.py
"""Defines the structure of the documentation"""

def print_list_integer(my_list=[]):
	"""This going to print the list of integer"""
	for i in range(len(my_list)):
		print("{:d}".format(my_list[i]))
