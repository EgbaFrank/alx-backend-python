#!/usr/bin/env python3
"""
Contains an async comprehension
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Return 10 random numbers via an async co-routine
    """

    return [num async for num in async_generator()]
