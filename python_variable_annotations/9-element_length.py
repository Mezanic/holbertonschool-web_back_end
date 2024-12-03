#!/usr/bin/env python3
"""This Module define the task 9"""


from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> list[tuple[Sequence, int]]:
    """Function  for task 9"""
    return [(i, len(i)) for i in lst]
