____author___: str = "730653429"


def manual_append(list: list[int], value: int) -> None:

    list.append(value)


def double(list_two: list[int]) -> None:
    index = 0
    while index in range(len(list_two)):
        list_two *= 2


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
