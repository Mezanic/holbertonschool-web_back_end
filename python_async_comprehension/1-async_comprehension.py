#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """call async generator for random number in a list"""
    return [i async for i in async_generator()]
