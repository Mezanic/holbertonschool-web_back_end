#!/usr/bin/env python3
"""This module define a function for create a tuple with string and float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple with string and float"""
    return (k, v * v)
