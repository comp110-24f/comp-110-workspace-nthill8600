____author___: str = "730653429"


def find_and_remove_max(lst: list[int]) -> int:
    if not lst:
        return -1

    max_value = max(lst)

    while max_value in lst:
        lst.remove(max_value)

    return max_value
