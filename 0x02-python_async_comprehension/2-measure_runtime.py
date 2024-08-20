#!/usr/bin/env python3
""" Implementing asyncio.gather() """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Timing concurrent async funcyions """
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total = time.time() - start
    return total
