#!/usr/bin/env python3
""" Complex types - functions module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function returning a callable function when passed a float argument """
    # function: Callable[[float], float] = make_multiplier
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
