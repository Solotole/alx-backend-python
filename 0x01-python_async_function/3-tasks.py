#!/usr/bin/env python3
""" Creating a task in the loop """
from typing import Any, Awaitable
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[Any]:
    """ returning a creted task """
    concurrent_obj = asyncio.create_task(wait_random(max_delay))
    return concurrent_obj
