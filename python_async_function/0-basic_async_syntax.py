#!/usr/bin/env python3
"""This Module define a function for a random delay between 0 and 10"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Create a random delay and wait this one for return it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
