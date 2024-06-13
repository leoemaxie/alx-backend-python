#!/usr/bin/env python3
"""Module that contains the function measure_time"""

from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the runtime of wait_n"""
    start_time = time()
    await wait_n(n, max_delay)
    return (time() - start_time) / n
