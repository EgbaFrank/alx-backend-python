#!/usr/bin/env python3
"""
Contains a type-annotated function 'to_kv'
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple from a str and [int or float]
    """
    return (k, v * v)
