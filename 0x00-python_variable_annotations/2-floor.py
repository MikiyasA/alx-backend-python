#!/usr/bin/env python3
"""
Write a type-annotated function floor which takes a float n
as argument and returns the floor of the float.
"""


def floor(n: float) -> int:
    """ type-annotated function floor takes a float
    and returns the floor of the float.
    return type is int """
    if n < 0:
        return (int(n - 1))
    return(int(n))
