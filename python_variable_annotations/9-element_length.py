#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list element lst as
argument and returns a list of integers representing the lengths of each
element in lst."""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of integers representing the lengths of
    each element in lst"""
    return [(i, len(i)) for i in lst]
