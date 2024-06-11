#!/usr/bin/env python3
"""Module for a function that returns a list of random integers"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """
    Function that returns a list of random integers
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
