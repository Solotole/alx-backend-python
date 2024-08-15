#!/usr/bin/env python3
""" sum of integers and floats """
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ sum of contents of a float and an integer """
    value = reduce(lambda x, y: x + y, mxd_lst)
    return float(value)
