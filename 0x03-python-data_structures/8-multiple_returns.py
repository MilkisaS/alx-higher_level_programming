#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """Returns the count of tuple"""
    count = len(sentence)
    if count == 0:
        first = None
        return count, first
    else:
        first == sentence[0]
        return count, first
