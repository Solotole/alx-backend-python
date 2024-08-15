#!/usr/bin/env python3
""" duck type annotations """
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ putting into place necessary annotations """
    return [(i, len(i)) for i in lst]
