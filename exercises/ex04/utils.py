"""List utility functions."""

__author__ = "730391001"


def all(xs: list[int], needle: int) -> bool:
    """Return true if equal to."""
    if len(xs) == 0:
        return False
    x: int = 0
    while x < len(xs):
        if xs[x] != needle:
            return False
        x += 1
    return True


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Return true of false if it matches."""
    if list_one == [] or list_two == []:
        if list_one == [] and list_two == []:
            return True
        else:
            return False
    
    if list_one > list_two or list_two > list_one:
        return False

    x: int = 0

    if len(list_one) > len(list_two):
        large_list = list_one
    else:
        large_list = list_two
    
    while x < len(large_list):
        if list_one[x] != list_two[x]:
            return False
        x += 1

    return True


def max(xs: list[int]) -> int:
    """Find Max from list."""
    if len(xs) == 0:
        raise ValueError("arg is an empty list")
    cur_max: int = xs[0]
    x: int = 1
    while x < len(xs):
        if xs[x] > cur_max:
            cur_max = xs[x]
        x += 1
    return cur_max