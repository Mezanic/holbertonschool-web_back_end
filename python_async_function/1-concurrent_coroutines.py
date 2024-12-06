#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_ramdom = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ doc a remplir """
    delay = [wait_ramdom(max_delay) for i in range(n)]
    all_delays = []
    for new_delay in asyncio.as_completed(delay):
        all_delays.append(await new_delay)
    return all_delays
