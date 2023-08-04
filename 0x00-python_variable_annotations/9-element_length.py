#!/usr/bin/env python3
"""Module that annotates a function"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in the input
    list and return a list of tuples.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, where
        each tuple contains a string element and its length.
    """
    return [(i, len(i)) for i in lst]
