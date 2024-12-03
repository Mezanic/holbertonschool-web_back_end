#!/usr/bin/env python3
"""This Module define the task 9"""


from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """Function  for task 9"""
    return [(i, len(i)) for i in lst]
