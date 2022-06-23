#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values with
Iterable[Sequence] & List[.Tuple[.Sequence, int]
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating lst with Iterable[Sequence] &
    return List[.Tuple[.Sequence, int]]"""
    return [(i, len(i)) for i in lst]
