#!/usr/bin/env python3

"""Module that returns a mixed type tuple"""
from typing import Tuple, Union, Optional


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k and the square of int/float v.

    Args:
        k (str): A string key.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the
        string k and the square of v as a float.
    """
    squared_value: float = float(v) ** 2
    return k, squared_value
