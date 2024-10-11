#!/usr/bin/env python3
"""
Contains a type annotated function
"""
from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return a list's first element or none"""
    if lst:
        return lst[0]
    else:
        return None
