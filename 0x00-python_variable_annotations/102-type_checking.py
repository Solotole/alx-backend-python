from typing import List, Sequence, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Zoom array- returning tuple of an array """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
