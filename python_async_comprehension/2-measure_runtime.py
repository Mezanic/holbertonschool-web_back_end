#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    result_time = start_time - end_time
    return result_time
