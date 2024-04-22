#!/usr/bin/python3
"""defines an async generator coroutine called async_generator
that takes no arguments."""

import asyncio
import random


async def async_generator():
    """Yield a random number between 0 and 10 every second."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
