"""List utility functions part 2."""

__author__ = "123456789"


def only_evens(xs: list[int]) -> list[int]:
    """Return list of even integers."""
    new_list: list[int] = []
    for item in xs:
        if item % 2 == 0:
            new_list.append(item)
    return new_list


def sub(s: list[int], start: int, end: int) -> list[int]:
    """Subset of a given list."""
    if s == [] or start >= end:
        return []
    elif start < 0:
        start = 0
    elif end > len(s):
        end = len(s)
    result: list[int] = []
    for i in range(start, end):
        result.append(s[i])
    return result


def concat(s: list[int], x: list[int]) -> list[int]:
    """Two lists into one."""
    result: list[int] = []
    for elt in s:
        result.append(elt)
    for elt_x in x:
        result.append(elt_x)
    return result
