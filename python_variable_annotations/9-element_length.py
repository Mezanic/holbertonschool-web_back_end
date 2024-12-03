#!/usr/bin/env python3
"""This Module define the task 9"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function  for task 9"""
    return [(i, len(i)) for i in lst]
