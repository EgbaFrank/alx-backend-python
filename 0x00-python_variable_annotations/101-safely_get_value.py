#!/usr/bin/env python3
"""
Contains a tpe annotated function
"""
from typing import Mapping, TypeVar, Union, Any


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
