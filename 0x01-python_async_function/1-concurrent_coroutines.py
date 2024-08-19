#!/usr/bin/env python3
""" appending a randonly generated float into a list """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def insertion_sort(return_list: List[float]) -> List[float]:
    """ insertion sort algorithm to sort list in ascending order """
    for i in range(1, len(return_list), 1):
        key = return_list[i]
        j = i - 1
        while j >= 0 and key < return_list[j]:
            return_list[j + 1] = return_list[j]
            j -= 1
        return_list[j + 1] = key
    return return_list


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ according to n loops appending randomly generated
        floats form a function
    """
    return_list = []
    for _ in range(n):
        value = await wait_random(max_delay)
        return_list.append(value)
    return_list = insertion_sort(return_list)
    return return_list
