#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ takes 2 arguments and returns a tuple """
    value: Tuple[str, float] = (k, v ** 2)
    return value
