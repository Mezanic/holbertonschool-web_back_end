#!/usr/bin/env python3
"""Module create generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """function for yield random float number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
