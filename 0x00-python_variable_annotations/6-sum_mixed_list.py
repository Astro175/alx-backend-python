#!/usr/bin/env python3
"""Module that returns a mixed type list"""
from typing import List, Optional, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum: float = 0

    for i in mxd_lst:
        sum += i
    return sum
