#!/usr/bin/env python3
""" Basic async generator """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, float]:
    """ randomly generating a float in a generator """
    await asyncio.sleep(1)
    for _ in range(10):
        yield random.uniform(0, 10)
