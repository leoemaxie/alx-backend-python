#!/usr/bin/env python3
"""
Module for a function that measures the total execution time for `n` coroutines
"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Function that measures the total execution time for `n` coroutines
    """
    start_time = time()
    await asyncio.gather(*[async_comprehension() for x in range(4)])
    end_time = time()
    return end_time - start_time
