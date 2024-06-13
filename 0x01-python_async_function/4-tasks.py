#!/usr/bin/env python3
"""Module that contains the function task_wait_n"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List:
    """
    Asynchronous coroutine that takes in 2 int arguments (n and max_delay)
    """
    result = []
    task = asyncio.create_task(
        (result.append(task_wait_random(max_delay)) for _ in range(n))
    )

    if task.done:
        return sorted(result)
