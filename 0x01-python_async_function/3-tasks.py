#!/usr/bin/env python3
""" Creating a task in the loop """
import asyncio
from typing import Any, Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[Any]:
    """ returning a creted task """
    concurrent_obj: Awaitable[Any] = asyncio.create_task(wait_random(max_delay))
    return concurrent_obj
