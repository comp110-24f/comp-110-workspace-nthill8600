"""Summing the elements of a list using different loops"""

____author___: str = "730653429"


def w_sum(vals: list[float]) -> float:
    total = 0.0
    index = 0

    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    total = 0.0

    for value in vals:
        total += value
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0.0

    for index in range(len(vals)):
        total += vals[index]
    return total
