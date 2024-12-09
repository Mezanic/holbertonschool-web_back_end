#!/usr/bin/env python3
"""Module create generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """function for yield random float number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
