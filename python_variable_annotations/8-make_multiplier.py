#!/usr/bin/env python3
"""This module define a function return a function for multiply multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function for multiply"""
    def multiply(value: float) -> float:
        """multiply multiplier"""
        product = value * multiplier
        return product
    return multiply
