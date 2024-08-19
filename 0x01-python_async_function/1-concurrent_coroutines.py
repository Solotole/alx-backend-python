#!/usr/bin/env python3
""" appending a randonly generated float into a list """
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns the list of all delays in ascending order."""
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Wait for each result and insert it in order
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert the delay in the correct position (keeping the list sorted)
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)
    
    return delays
