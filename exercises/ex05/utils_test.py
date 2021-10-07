"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def test_only_evens_empty_list() -> None:
    """Test for empty list."""
    assert only_evens([]) == []


def test_only_evens_all_evens() -> None:
    """Test for all even list."""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_only_evens_with_odds() -> None:
    """Test for all odd and even list."""
    assert only_evens([1, 2, 3, 6, 7, 9, 12]) == [2, 6, 12]


def test_sub_one() -> None:
    """input."""
    assert sub([1, 2, 3, 5], 3, 5) == [2, 3]


def test_sub_two() -> None:
    """One element."""
    assert sub([1], 2, 3) == [1]


def test_sub_three() -> None:
    """Return empty list."""
    assert sub([], 1, 3) == []


def test_concat_one() -> None:
    """first test."""
    assert concat([2], [3]) == [2, 3]


def test_concat_two() -> None:
    """Multiple lists."""
    assert concat([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


def test_concat_three() -> None:
    """Don't return the empty list"""
    assert concat([], [1]) == [1]
