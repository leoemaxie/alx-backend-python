#!/usr/bin/env python3
"""Module for Async Generator"""

from random import uniform
from time import sleep
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    Async Generator that yields a random number between 0 and 10 every second
    """
    for i in range(10):
        sleep(1)
        yield uniform(0, 10)
