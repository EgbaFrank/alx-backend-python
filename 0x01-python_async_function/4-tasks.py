#!/usr/bin/env python3
"""
Contains an async function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    done = []
    for task in asyncio.as_completed(tasks):
        done.append(await task)

    return done
