#!/usr/bin/env python3
"""Type-annotated function safe_first_element that takes a list lst of
any type elements and returns the first element of the list."""
from typing import Optional, Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst if there is any, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
