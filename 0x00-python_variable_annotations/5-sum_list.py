#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """ summing up elements of a list and returning float """
    value = reduce(lambda x, y: x + y, input_list)
    return float(value)
