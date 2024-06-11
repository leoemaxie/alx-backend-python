#!/usr/bin/env python3
"""Module for Async Generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    Async Generator that yields a random number between 0 and 10 every second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
