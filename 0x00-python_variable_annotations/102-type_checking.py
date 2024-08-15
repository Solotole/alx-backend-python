#!/usr/bin/env python3
""" Type Checking """
from typing import List, Sequence, Tuple, Union


def zoom_array(
    lst: Union[List[int], Tuple[int, ...]], factor: int = 2
) -> List[int]:
    """ Zoom array- returning tuple of an array """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
