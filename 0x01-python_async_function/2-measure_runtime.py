#!/usr/bin/env python3
""" Timing of time taken for Coroutine complition """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measuring time taken for an async function to run"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total = time.time() - start
    return total / n
