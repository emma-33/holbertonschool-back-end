#!/usr/bin/python3
"""Type-annotated function safely_get_value that returns the value of a key
in a dictionary."""
from typing import Union, Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value of the key in the dictionary if it exists,
    otherwise None"""
    if key in dct:
        return dct[key]
    else:
        return default
