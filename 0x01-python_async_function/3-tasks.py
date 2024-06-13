#!/usr/bin/env python3
"""
This module contains the task_wait_random function
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that takes in an integer argument (max_delay)
    and returns a asyncio Task.
    """
    return asyncio.Task(wait_random(max_delay))
