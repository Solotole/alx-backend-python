#!/usr/bin/env python3
""" Basic coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Async function that returns a random float between
        0 and max_delay
    """
    return random.uniform(0, max_delay)
