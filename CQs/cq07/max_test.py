____author___: str = "730653429"


from find_max import find_and_remove_max


def test_return_value() -> None:
    nums = [1, 2, 3, 4, 5]
    result = find_and_remove_max(nums)
    assert result == 5


def test_mutation() -> None:
    nums = [1, 2, 3, 4, 5]
    find_and_remove_max(nums)
    assert 5 not in nums
    assert nums == [1, 2, 3, 4]


def test_edge_case() -> None:
    nums = [6]
    result = find_and_remove_max(nums)
    assert result == 6
    assert nums == []
