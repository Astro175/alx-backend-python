#!/usr/bin/env python3

"""Returns sum of variable in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
      A type-annotated function sum_list which takes
      a list input_list of floats as argument
      and returns their sum as a float.
    """
    sum: float = 0

    for i in input_list:
        sum += i
    return sum
