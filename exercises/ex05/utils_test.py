"""Define and test our utility functions!"""

____author___: str = "730653429"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_empty() -> None:
    assert only_evens([]) == []  # test that it returns empty list


def test_only_evens_negatives() -> None:
    assert only_evens([-4, -3, -2, -1]) == (
        [-4, -2]
    )  # test that it works with negatives


def test_only_evens_not_mutate() -> None:  # tests that it does not mutate given list
    list = [1, 2, 3, 4, 5]
    only_evens(list)
    assert list == [1, 2, 3, 4, 5]


def test_sub_empty() -> None:  # test that it works with empty list
    assert sub([], 0, 1) == []


def test_sub_valid_indexes() -> None:  # test that valid indexes are turned
    assert sub([1, 2, 3, 4, 5], 1, 4) == [1, 5]


def test_sub_not_mutate() -> None:  # test that the function doesn't mutate orginal list
    list = [1, 2, 3, 4, 5]
    sub(list, 1, 4)
    assert list == [1, 2, 3, 4, 5]


def test_add_at_index_raises_indexerror():  # tests that an index error
    # is raised if out of bounds
    list = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(list, 5, 4)


def test_add_at_index_valid_insert() -> (
    None
):  # tests that it inserts element at right index
    list = [1, 2, 3]
    add_at_index(list, 4, 1)
    assert list == [1, 4, 2, 3]


def test_add_at_index_not_mutate() -> (
    None
):  # tests that the orginal list is not mutated
    list = [1, 2, 3, 4]
    add_at_index(list, 5, 3)
    assert list == [1, 2, 3, 5, 4]
