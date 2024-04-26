#!/usr/bin/env python3
"""defines an coroutine called async_comprehension
that takes no arguments."""
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Collect 10 random numbers using an async comprehensing over
    an async generator"""
    return [i async for i in async_generator()]
