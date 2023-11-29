#!/usr/bin/python3
"""Implements the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        
