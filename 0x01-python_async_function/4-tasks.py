#!/usr/bin/env python3
""" Module to call on a created task """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
insertion_sort = __import__('1-concurrent_coroutines').insertion_sort


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ calling an already created task """
    return_list = []
    for _ in range(n):
        value = await task_wait_random(max_delay)
        return_list.append(value)
    return_list = insertion_sort(return_list)
    return return_list
