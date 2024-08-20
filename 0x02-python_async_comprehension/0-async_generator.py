#!/usr/bin/env python3
""" Basic async generator """
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """ randomly generating a float in a generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
