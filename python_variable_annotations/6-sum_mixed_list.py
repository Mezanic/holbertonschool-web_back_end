#!/usr/bin/env python3
"""This module define a function for returm sum from mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum from mixed list"""
    return sum(mxd_lst)
