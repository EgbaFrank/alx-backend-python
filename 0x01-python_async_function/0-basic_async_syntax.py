#!/usr/bin/env python3
"""
Contains an async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    Args:
        max_delay (int): Maximum delay in seconds (default: 10)

    Returns:
        float: Actual delay waited
    """
    delay_for = random.uniform(0, max_delay)
    await asyncio.sleep(delay_for)

    return delay_for
