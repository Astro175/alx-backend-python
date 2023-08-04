#!/usr/bin/env python3

"""Module that returns a callback function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by the
    given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the result of multiplication.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
