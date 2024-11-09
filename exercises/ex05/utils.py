"""Implement utility functions!"""

____author___: str = "730653429"


def only_evens(list_one: list[int]) -> list[int]:
    even_numbers: list[int] = []  # create an empty list that will store even numbers
    for index in range(len(list_one)):  # confirm its within list length
        if list_one[index] % 2 == 0:  # if returns 0, means its a even number
            even_numbers.append(list_one[index])

    return even_numbers


def sub(list_one: list[int], start: int, end: int) -> list[int]:
    if len(list_one) == 0 or start >= len(list_one) or end <= 0:
        return []  # if input list is empty or invalid indexes

    if start < 0:
        start = 0  # adjust the start index if its negative

    if end > len(list_one):
        end = len(list_one)  # change the end index if longer than the lsit

    subset = []  # create empty list
    for index in range(start, end):
        subset.append(list_one[index])  # add each element to the subset

    return subset


def add_at_index(list_one: list[int], element_add: int, element_index: int) -> None:
    if element_index < 0 or element_index > len(
        list_one
    ):  # sees if the index is out of bounds
        raise IndexError("Index is out of bounds for the input list")

    list_one.append(0)  # add space to the list

    for index in range(
        len(list_one) - 1, element_index, -1
    ):  # shifts the elements to make space
        list_one[index] = list_one[index - 1]

    list_one[element_index] = element_add  # adds the new element at the correct index
