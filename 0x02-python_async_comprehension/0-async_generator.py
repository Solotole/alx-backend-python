#!/usr/bin/env python3
""" Basic async generator """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, float]:
    """ randomly generating a float in a generator """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
