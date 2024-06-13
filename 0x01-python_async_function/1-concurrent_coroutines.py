#!/usr/bin/env python3
"""Module that contains the function wait_n"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """
    Asynchronous coroutine that takes in 2 int arguments (n and max_delay)
    and returns a list of n floats, each representing the delay time for each
    coroutine sorted in ascending order.
    """
    result = []
    task = asyncio.create_task(
        (result.append(wait_random(max_delay)) for _ in range(n))
    )

    if task.done:
        return sorted(result)
