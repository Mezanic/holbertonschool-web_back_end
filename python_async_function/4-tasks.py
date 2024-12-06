#!/usr/bin/env python3
"""Task 4 for project async python"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """"""
    delay = [task_wait_random(max_delay) for i in range(n)]
    all_delays = []
    for new_delay in asyncio.as_completed(delay):
        all_delays.append(await new_delay)
    return all_delays
