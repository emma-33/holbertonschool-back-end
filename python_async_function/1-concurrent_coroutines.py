#!/usr/bin/env python3
"""async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    list_delays = [wait_random(max_delay) for i in range(n)]

    delays = []
    for delay in asyncio.as_completed(list_delays):
        delays.append(await delay)
    return sorted(delays)
