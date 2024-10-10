#!/usr/bin/env python3
"""
Contains a type-annotated function element length
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of each element in a list"""
    return [(i, len(i)) for i in lst]
