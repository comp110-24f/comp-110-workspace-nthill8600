____author___: str = "730653429"

"List utility functions!"


def all(list: list[int], integer: int) -> bool:
    if len(list) == 0:
        return False  # if the list is empty will return false

    count = 0
    while count < len(list):
        if list[count] != integer:  # if its not a match return false
            return False
        count += 1  # to cycle through the indexes

    return True


def max(list_two: list[int]) -> int:
    if len(list_two) == 0:
        raise ValueError("max() arg is an empty list")  # given to us

    maxium = list_two.pop()  # define the maximum

    while len(list_two) > 0:
        current = list_two.pop()
        if current > maxium:  # if the current number is greater than the maxium
            maxium = current  # than the current will become the maxium
    return maxium


def is_equal(one_list: list[int], two_list: list[int]) -> bool:
    if len(one_list) != len(two_list):
        return False  # if they don't exactly match return false

    while len(one_list) > 0:
        if one_list.pop() != two_list.pop():
            return False

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    while len(list2) > 0:
        list1.append(list2[0])  # add an element to the end of the lsit
        list2.pop(0)  # uses pop function to remove the last element
